import streamlit as st

st.title("Marks Calculator")

m1 = st.number_input("Subject 1")
m2 = st.number_input("Subject 2")

total = m1 + m2

if st.button("Calculate"):
    st.write("Total Marks:", total)