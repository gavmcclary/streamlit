import streamlit as st
from openai import OpenAI

try:
    client = OpenAI(api_key=st.text_input('Enter OpenAI API token:', type='password'),)
    st.success('Proceed to entering your prompt message!', icon='👉')
except:
    pass

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

