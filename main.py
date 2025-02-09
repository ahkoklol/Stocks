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
st.title("📈 Stock Market Expert Chatbot with File Upload")

# Initialize chat session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a stock market expert specializing in financial insights, investment strategies, and stock analysis. Provide data-driven advice and clear explanations."}
    ]

# File uploader
uploaded_file = st.file_uploader("Upload a financial report (PDF, CSV, TXT)", type=["pdf", "csv", "txt"])

file_content = ""

if uploaded_file:
    file_name = uploaded_file.name.lower()
    
    if file_name.endswith(".txt"):
        file_content = uploaded_file.getvalue().decode("utf-8")

    elif file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        file_content = df.to_string()

    elif file_name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            file_content += page.extract_text() + "\n"

    st.success(f"Uploaded: {file_name}")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask about stock market trends, investment strategies, or specific stocks..."):
    # If a file is uploaded, add its content to the prompt
    if file_content:
        prompt = f"User query: {prompt}\n\nFinancial Document Data:\n{file_content[:5000]}"  # Truncate if too long

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

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
                full_reply += token  # Append token to full reply
                reply_container.markdown(full_reply)  # Update the placeholder

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_reply})
