import streamlit as st
import pandas as pd
import numpy as np
import os
from openai import OpenAI

client = OpenAI(api_key = os.environ.get('OPENAI_API_KEY'))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)


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
