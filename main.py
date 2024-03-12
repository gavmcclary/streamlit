import streamlit as st
from openai import OpenAI

try:
    client = OpenAI(api_key=st.text_input('Enter OpenAI API token:', type='password'),)
    st.success('Proceed to entering your prompt message!', icon='👉')
except Exception as e:
    st.text(e)
