import streamlit as st
from langchain_community.llms import Ollama
import PyPDF2

st.set_page_config(page_title="Dual Chatbot", layout="wide")
st.title("🤖 Dual Chatbot (Final Working)")

# Load local model
llm = Ollama(model="llama3")

# Mode selection
mode = st.radio("Choose Mode:", ["Normal Chat", "Document Chat"])

# ================= NORMAL CHAT =================
if mode == "Normal Chat":
    st.subheader("💬 Normal Chatbot")

    query = st.text_input("Ask anything:")

    if query:
        response = llm.invoke(query)
        st.write("🤖 Answer:", response)

# ================= DOCUMENT CHAT =================
elif mode == "Document Chat":
    st.subheader("📄 Document Chatbot")

    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        query = st.text_input("Ask question from document:")

        if query:
            prompt = f"""
            Answer the question based only on the document below.

            Document:
            {text}

            Question:
            {query}
            """

            response = llm.invoke(prompt)
            st.write("📄 Answer:", response)