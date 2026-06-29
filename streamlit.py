import streamlit as st
import pandas as pd


# Page Title
st.title("🎓 Student Result Analyzer")


# User Input

name = st.text_input("Enter Student Name")

mark1 = st.number_input(
    "Enter Python Mark",
    min_value=0,
    max_value=100
)

mark2 = st.number_input(
    "Enter AI Mark",
    min_value=0,
    max_value=100
)

mark3 = st.number_input(
    "Enter Database Mark",
    min_value=0,
    max_value=100
)


# Button

if st.button("Calculate Result"):

    total = mark1 + mark2 + mark3
    average = total / 3


    if average >= 90:
        grade = "A+"

    elif average >= 80:
        grade = "A"

    elif average >= 70:
        grade = "B"

    elif average >= 50:
        grade = "C"

    else:
        grade = "Fail"


    st.success("Result Generated")


    st.write("Student Name:", name)

    st.write("Total Mark:", total)

    st.write("Average:", average)

    st.write("Grade:", grade)



    # Table Display

    data = {
        "Name":[name],
        "Python":[mark1],
        "AI":[mark2],
        "Database":[mark3],
        "Average":[average],
        "Grade":[grade]
    }


    df = pd.DataFrame(data)

    st.dataframe(df)