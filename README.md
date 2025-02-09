# Investment Tracker Web App

## Overview
The **Investment Tracker Web App** is a Python-based application designed to help users manage their investments efficiently. This app leverages the **yFinance API** to track real-time stock price variations, fetch news updates related to user portfolios, and provide AI-driven investment insights using transformer neural network models. Additionally, it incorporates machine learning pipeline to analyze financial statements,  assess company sentiments and predict stock prices. Meta Llama 3 will be used as Large Language Model (LLM) with a local Ollama server to run a sentiment analysis of recent financial new headlines scraped from the web using the News API. 

## Features
- **AI Stock Price Prediction**: Use Large Language Models in Python to predict stock prices.
- **Real-time Stock Tracking**: Monitor stock prices and their variations using the yFinance API.
- **Personalized News Feed**: Receive relevant news based on the stocks in the user's portfolio.
- **LLM Investment Advice**: Get AI-generated investment advice by leveraging a large language model (LLM).
- **Deep Learning Analysis**:
  - Evaluate financial statements for insights into company performance.
  - Perform sentiment analysis on company-related news and reports.
- **Stock Price Prediction**: Implement machine learning models to forecast stock trends.
- **Portfolio Risk Assessment**: AI-driven analysis of portfolio risk and diversification.
- **Automated Market Alerts**: Receive alerts on significant market movements and stock price changes.
- **Options & Derivatives Analysis**: Advanced quantitative tools for evaluating options, derivatives, and hedging strategies.
- **AI-powered Technical Analisys**: Use AI to interpret stock charts based on technical analysis.
- **AI Agents Analysis of Financial Documents**: Use AI to extract meaningful insights for stock market analysis from financial documents like company annual reports (Form 10-K).

## Tech Stack
- **Backend**: Python, Streamlit
- **APIs & Data Sources**:
  - yFinance API (Real-time stock data)
  - News API (Financial news updates)
  - OpenAI/LLM API (Investment advisory)
- **Deep Learning & Machine Learning Frameworks**:
  - TensorFlow/PyTorch (Financial statement analysis)
  - NLP Models (Sentiment analysis, market news processing)
  - Scikit-Learn (Stock prediction models, quantitative finance calculations)
- **Frontend**: Streamlit (UI Framework)
- **Database**: Firestore (Cloud Firestore for user data & portfolio storage)
- **Deployment**: Docker, AWS/GCP/Azure

