import streamlit as st
import openai

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai.api_key = st.secrets['OPENAI_API_KEY']
    else:
        openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')


with st.chat_message("user"):

  input = None

  st.write("Hello 👋")
  input = st.chat_input("Say something")
  if input == None:
    st.write("")
  else:
    st.write("You said: ", input)
    st.balloons()

# Code blocks
with st.echo():
  print('Code will be executed and printed')
