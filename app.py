import pandas as pd
import streamlit as st

uploaded_file = st.file_uploader("Upload an excel file", type=["csv", "xlsx", "xls"])

api_key = st.text_input("Enter your OpenAI API Key")
api_key = st.secrets.openai_credentials.api_key

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()
    st.write("File Name:", uploaded_file.name)
    st.write("File Content:")
    if file_extension == "csv":
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)
    st.write(data)
