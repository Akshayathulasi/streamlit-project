import streamlit as st

# Page settings
st.set_page_config(
    page_title="AI Sentiment Analyzer",
    page_icon="🤖"
)

# Title
st.title("🤖 AI Sentiment Analyzer")

st.write("Enter a sentence and AI will detect sentiment")

# Input box
text = st.text_area("Enter your text")


# Simple AI logic
def predict_sentiment(text):

    positive_words = [
        "good",
        "great",
        "happy",
        "excellent",
        "love",
        "amazing"
    ]

    negative_words = [
        "bad",
        "worst",
        "sad",
        "hate",
        "poor"
    ]


    text = text.lower()

    for word in positive_words:
        if word in text:
            return "😊 Positive"

    for word in negative_words:
        if word in text:
            return "😞 Negative"

    return "😐 Neutral"



# Button
if st.button("Analyze"):

    if text == "":
        st.warning("Please enter text")

    else:
        result = predict_sentiment(text)

        st.success(result)


# Sidebar
st.sidebar.title("About")

st.sidebar.write(
"""
This is a basic AI project.

Technology:
- Python
- Streamlit
- NLP
"""
)