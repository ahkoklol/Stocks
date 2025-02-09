import streamlit as st
from openai import OpenAI
import pandas as pd
import PyPDF2

# Load API Key from secrets
secret_key = st.secrets["OPENAI_API_KEY"]["key"]

# Initialize OpenAI client for Mistral API
client = OpenAI(
    base_url="https://api.mistral.ai/v1/",
    api_key=secret_key,
)

# Set up Streamlit UI
st.title("Stock Market Expert Chatbot")

# Initialize session state for messages & uploaded file content
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a stock market expert specializing in financial insights, investment strategies, and stock analysis. Provide data-driven advice and clear explanations. Give insights on whether to invest in the analyzed company or not (yes or no response)."}
    ]

if "uploaded_files_content" not in st.session_state:
    st.session_state.uploaded_files_content = ""

# Multiple file uploader
uploaded_files = st.file_uploader(
    "Upload financial reports (PDF, CSV, TXT)", 
    type=["pdf", "csv", "txt"], 
    accept_multiple_files=True
)

# Process uploaded files
if uploaded_files:
    new_file_content = ""
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name.lower()
        file_content = ""

        if file_name.endswith(".txt"):
            file_content = uploaded_file.getvalue().decode("utf-8")

        elif file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            file_content = df.to_string()

        elif file_name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                file_content += page.extract_text() + "\n"

        new_file_content += f"\n\n--- File: {file_name} ---\n\n" + file_content[:5000]  # Truncate large files
        st.success(f"Uploaded: {file_name}")

    # **Store uploaded file contents persistently**
    st.session_state.uploaded_files_content += new_file_content

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])  # ✅ Use `st.write()` for better formatting

# User input
if prompt := st.chat_input("Ask about stock market trends, investment strategies, or specific stocks..."):
    # Include stored file contents in the prompt
    final_prompt = f"User query: {prompt}\n\nFinancial Document Data:\n{st.session_state.uploaded_files_content}"

    st.session_state.messages.append({"role": "user", "content": final_prompt})

    with st.chat_message("user"):
        st.write(prompt)

    # Get response from Mistral 7B
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="open-mistral-7b",
            messages=st.session_state.messages,
            stream=True  # Enables streaming response
        )

        # Display streaming response correctly
        full_reply = ""
        reply_container = st.empty()  # Create a placeholder for dynamic updates
        for chunk in response:
            token = chunk.choices[0].delta.content
            if token:
                full_reply += token.replace("_", "\\_").replace("*", "\\*")  # ✅ Escape Markdown special characters
                reply_container.write(full_reply)  # ✅ Use `st.write()` for proper formatting

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_reply})
