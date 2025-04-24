from codeext import CodeExtractor
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()
st.title("Video Code Extractor")
st.caption("Extract code from any type of  coding video in one click")
file_upload = st.file_uploader("Upload Video", type=["mp4", "mov", "avi"])

if file_upload:
    extractor = CodeExtractor(file_upload)

    with open("extracted_text.txt", "r") as f:
        text = f.read()

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    response = llm.invoke(f"Please fix the provided code without adding any explanations or comments. Remove any duplicate or unnecessary code. Provide only the corrected code: {text}").content


    st.subheader("Fixed Code:")
    st.code(response, language="python")
