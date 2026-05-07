import streamlit as st
import requests
import os

st.title("🤖 AI Chatbot")

# API Key from Render Environment Variable
API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API URL
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://render.com",
    "X-Title": "AI Chatbot"
}

user_input = st.text_input("Ask me anything")

if user_input:

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    data = response.json()

    try:
        answer = data["choices"][0]["message"]["content"]
        st.write("🤖", answer)

    except:
        st.write(data)