import streamlit as st
import requests

# Set up the API endpoint and headers
API_URL = "https://api-inference.huggingface.co/models/avichr/heBERT_sentiment_analysis"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit app
def main():
    st.title("Sentiment Analysis with heBERT")
    
    # Text input for the user to enter a sentence/tweet
    user_input = st.text_area("Enter a sentence or tweet:", "")
    
    # Button to trigger the sentiment analysis
    if st.button("Analyze Sentiment"):
        if user_input:
            with st.spinner("Analyzing..."):
                result = query({"inputs": user_input})
                # Display the sentiment analysis result
                st.write("Sentiment Analysis Result:")
                st.json(result)
        else:
            st.warning("Please enter a sentence or tweet to analyze.")

if __name__ == "__main__":
    main()
