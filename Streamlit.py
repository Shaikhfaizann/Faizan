import streamlit as st
import pandas as pd
import numpy as np

st.write("Faizan")

df = pd.DataFrame({
  'first column': ["a", "b", "c", "d"],
  'second column': [10, 20, 30, 40]
})

st.write(df)

st.table(df)
st.line_chart(df)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.0760, 72.8777],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.button("x")

st.selectbox(options=["dkfk","d"],label="d")

st.text_input("Your name", key="name")
st.number_input("df")

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)