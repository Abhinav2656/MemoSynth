from fastapi import FastAPI, Request
from sentence_transformers import SentenceTransformer
import redis, uuid, httpx, os
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()

# Correct new-style client initialization
chroma_client = chromadb.HttpClient(host="localhost", port=8000)

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")
redis_client = redis.Redis.from_url(os.getenv("REDIS_URL"))
collection = chroma_client.get_or_create_collection("memory")

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    message = data["message"]
    user_id = data.get("user_id", "demo")

    # Embed and store
    embedding = model.encode(message).tolist()
    msg_id = str(uuid.uuid4())
    collection.add(documents=[message], embeddings=[embedding], ids=[msg_id], metadatas=[{"user": user_id}])

    # Store user message in Redis with role
    redis_client.lpush(f"chat:{user_id}", f"user|{message}")
    redis_client.ltrim(f"chat:{user_id}", 0, 19)  # Store the last 20 exchanges

    # Retrieve message history from Redis
    history = redis_client.lrange(f"chat:{user_id}", 0, -1)
    messages = []
    for entry in reversed(history):  # reverse to maintain order
        decoded = entry.decode()  # decode bytes to string
        if "|" in decoded:
            role, content = decoded.split("|", 1)
            messages.append({"role": role, "content": content})

    # Semantic search on Chroma collection for context
    results = collection.query(query_embeddings=[embedding], n_results=3)
    memory = "\n".join(results["documents"][0]) if results["documents"] else ""

    # Groq completion (using an external API for the bot's reply)
    headers = {"Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-r1-distill-llama-70b",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant with memory."},
            {"role": "user", "content": f"Context:\n{memory}\n\nUser: {message}"}
        ]
    }

    async with httpx.AsyncClient() as client:
        try:
            res = await client.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
            res.raise_for_status()  # This will raise an HTTPError if the status code is 4xx/5xx
            reply = res.json()["choices"][0]["message"]["content"]
        except httpx.HTTPStatusError as e:
            return {"error": f"Request failed with status {e.response.status_code}"}
        except httpx.RequestError as e:
            return {"error": f"Request error: {str(e)}"}

    # Store assistant's reply in Redis
    redis_client.lpush(f"chat:{user_id}", f"assistant|{reply}")
    redis_client.ltrim(f"chat:{user_id}", 0, 19)

    return {"reply": reply}
