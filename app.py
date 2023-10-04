import pandas as pd
import streamlit as st
import os
from langchain.agents import create_pandas_dataframe_agent 
from langchain.llms import OpenAI

uploaded_file = st.file_uploader("Upload an excel file", type=["csv", "xlsx", "xls"])

api_key = st.text_input("Enter your OpenAI API Key")
api_key = st.secrets.openai_credentials.api_key

os.environ['OPENAI_API_KEY'] = api_key

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()
    st.write("File Name:", uploaded_file.name)
    st.write("File Content:")
    if file_extension == "csv":
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)
    st.write('File loaded successfully.')
    agent = create_pandas_dataframe_agent(OpenAI(temperature=0), data, verbose=True) 
    openai = OpenAI(temperature=0.0) 
    st.write(openai.model_name)
    prompt = st.text('What would you like to do?')

    if prompt is not None and api_key is not None:
        agent(prompt)