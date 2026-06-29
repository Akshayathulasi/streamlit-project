import streamlit as st
import pickle


# Load model
model = pickle.load(open("model.pkl","rb"))

vectorizer = pickle.load(open("vectorizer.pkl","rb"))


st.title("Fake Review Detection")


review = st.text_area(
    "Enter Product Review"
)


if st.button("Check Review"):


    # Convert text to numbers
    review_vector = vectorizer.transform([review])


    # Prediction
    result = model.predict(review_vector)


    if result[0] == 1:
        st.error("Fake Review")

    else:
        st.success("Real Review")