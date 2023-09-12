# Sentiment Analysis App

This project implements a simple sentiment analysis application using Streamlit, Langchain, and the Replicate API with the LLama 2 70B model.

## Overview

The app takes in user input text and analyzes the sentiment as either positive, negative, or neutral. It uses the LLama 2 70B model from Replicate to generate the sentiment analysis.

The app is built using Streamlit for the UI and Langchain for chaining the prompt to the Replicate API.

Preview:
[sentiment_analyser_shot](https://github-production-user-asset-6210df.s3.amazonaws.com/131486782/265725391-6d73a8d2-6648-45c7-b9af-d779c1d190ad.jpg)

## Setup

### Install requirements

```
pip install streamlit langchain python-dotenv
```

### Set up API key 

Sign up for a free API key at [Replicate](https://replicate.com/).

Add the key to a `.env` file:

```
REPLICATE_API_TOKEN="YOUR_API_KEY"
```

### Run the app

```
streamlit run app.py
```

The app will be served at http://localhost:8501.

## Workflow

- The user enters text input which is captured by Streamlit
- The input text is passed to a Langchain `PromptTemplate` with a template for sentiment analysis
- Langchain chains this to a call to the Replicate API with the LLama 2 70B model 
- Replicate returns the sentiment prediction and score
- The prediction is displayed back to the user in the Streamlit interface

## Next Steps

- Add user authentication
- Deploy the app to a server for public access
- Containerize the app with Docker
- Improve the prompt engineering for more accurate predictions
- Add more customizations like sentiment thresholds
