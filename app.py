import streamlit as st
import requests

st.set_page_config(page_title="MemoSynth", layout="centered")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🧠 MemoSynth Chatbot")

# Display chat history
for role, msg in st.session_state.history:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}")

# Text input at bottom
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.history.append(("user", user_input))
    try:
        res = requests.post("http://localhost:8001/chat", json={"message": user_input})
        res.raise_for_status()
        reply = res.json().get("reply", "Error: No reply received.")
    except Exception as e:
        reply = f"Error: {e}"
    
    # Append bot response and display
    st.session_state.history.append(("bot", reply))
    st.rerun()
