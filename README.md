# MemoSynth - AI Memory-Enhanced Chatbot

MemoSynth is an AI-powered chatbot application that remembers past interactions and provides relevant context-based responses to users. The chatbot uses state-of-the-art language models and memory storage to maintain a continuous conversation history, allowing it to deliver smarter and more context-aware responses.

This project is built using **FastAPI** for the backend, **Streamlit** for the frontend, and integrates with **Groq** for generating AI responses, **Redis** for session memory storage, and **Chroma** for semantic search.

## Features

- **Contextual Conversations**: The bot remembers past interactions and uses that context to provide relevant responses.
- **Memory Management**: Stores and recalls user interactions using Redis and Chroma.
- **Easy Setup**: Simple environment configuration to get the bot up and running.
- **Modern UI**: Built with Streamlit for an interactive and user-friendly interface.
- **AI Integration**: Uses Groq for generating context-aware responses.

## Project Structure

- **/main.py**: Contains the FastAPI backend logic, including memory management, AI model interaction, and API routing.
- **/app.py**: Streamlit frontend for interacting with the user. It sends user input to the FastAPI backend and displays responses.
- **/.env**: Contains environment variables like API keys and URLs.
- **/requirements.txt**: Lists all the required Python dependencies for the project.
- **/.gitignore**: Excludes unnecessary files from version control (e.g., environment files, Redis data).

## Prerequisites

- **Python 3.8+**
- **Redis**: Make sure Redis is running locally or through a cloud service.
- **Chroma**: For memory and semantic search management.
- **Groq API Key**: Needed to generate AI responses from Groq.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MemoSynth.git
cd MemoSynth

### 2. Install Dependencies : Make sure to create a virtual environment first.

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a .env file in the root directory and add your environment variables.

```env
REDIS_URL=redis://localhost:6379
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run Redis
If Redis is not installed, you can download and run it from here. To run Redis locally:

```bash
redis-server
```

### 5. Run the Application
To start the backend:

```bash
uvicorn main:app --reload
```

### To start the frontend (Streamlit app):

```bash
streamlit run app.py
```

### 6. Access the Application
Once both the backend and frontend are running, open your browser and go to:

```text
http://localhost:8501
```

Usage
Start the conversation: Type a message in the input box.

Memory: The bot will remember your previous messages and provide responses based on the context.

Interaction: Keep chatting, and the bot will update its memory, generating responses that refer back to earlier conversations.

## Architecture
-**Backend (FastAPI)**: Handles API requests, interacts with Redis for storing user messages, and performs semantic searches using Chroma.

-**Frontend (Streamlit)**: Provides an interactive interface where users can send and receive messages. It communicates with the FastAPI backend.

-**Memory Storage (Redis)**: Used to store recent conversations in memory, allowing the bot to retain context.

-**Semantic Search (Chroma)**: Used to retrieve past conversations based on message similarity, enabling the bot to recall relevant context.

-**AI Generation (Groq)**: Processes the context and user input to generate the chatbot's response.

Contributing
We welcome contributions to MemoSynth! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature (git checkout -b feature-branch).

Commit your changes (git commit -am 'Add new feature').

Push to your fork (git push origin feature-branch).

Open a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
FastAPI: Web framework for building APIs with Python.

Streamlit: A framework for building interactive web apps in Python.

Redis: In-memory key-value store for fast data storage.

Chroma: For memory management and semantic search.

Groq: API for generating AI responses.