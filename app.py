import streamlit as st
import requests
import os

st.title("🤖 AI Chatbot")

# Get API key from Render environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API URL
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# User input
user_input = st.text_input("Ask me anything")

if user_input:

    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()

    # Display response
    try:
        answer = data["choices"][0]["message"]["content"]
        st.write("🤖", answer)

    except:
        st.write(data)