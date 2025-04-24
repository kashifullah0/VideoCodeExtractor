from codeext import CodeExtractor
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()
google_api_key = "AIzaSyBkA9oQFyqX-BEgq1skdzxghxd0_G0494E"
st.title("Video Code Extractor")

file_upload = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])

if file_upload:
    extractor = CodeExtractor(file_upload)

    with open("extracted_text.txt", "r") as f:
        text = f.read()

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                 google_api_key=google_api_key)

    response = llm.invoke(f"I am providing you code, fix it do not add any explanation or comment: {text}").content

    st.subheader("Fixed Code:")
    st.code(response, language="python")
