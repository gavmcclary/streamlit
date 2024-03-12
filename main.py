import streamlit as st
import pandas as pd
import numpy as np
import os

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
