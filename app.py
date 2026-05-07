import streamlit as st
import requests
import os

st.title("🤖 Online AI Chatbot")

API_KEY = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

user_input = st.text_input("Ask something:")

if user_input:

    payload = {
        "model": "openchat/openchat-7b",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()

    try:
        answer = data["choices"][0]["message"]["content"]
        st.write("🤖 Answer:", answer)
    except:
        st.write(data)