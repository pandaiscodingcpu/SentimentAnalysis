import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App")

text = st.text_area("Enter a sentence to analyze its sentiment:")

if st.button("Analyze"):
    if text:
        blob = TextBlob(text)
        pol = blob.sentiment.polarity

        if pol > 0:
            sentiment = "Positive 😊"
        elif pol < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Polarity Score:** {pol}")
    else:
        st.warning("Please enter some text to analyze.")
