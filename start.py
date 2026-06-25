import streamlit as st


















st.title("My First Streamlit App")
st.write("Hello! I am learning Streamlit 😄")

st.title("Big Title")
st.header("Header")
st.subheader("Small Header")
st.write("Any text")

name = st.text_input("Enter your name")
st.write("Hello", name)

if st.button("Click me"):
    st.write("Button clicked!")

age = st.slider("Select age", 0, 100)
st.write("Age:", age)

option = st.selectbox("Choose one", ["AI", "ML", "Web"])
st.write(option)

import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "marks": [10, 20, 30, 40]
})

st.line_chart(data)