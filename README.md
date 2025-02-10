# Investment Tracker Web App

## Overview
The **Investment Tracker Web App** is a Python-based application designed to help users manage their investments efficiently. This app leverages the **yFinance API** to track real-time stock price variations, fetch news updates related to user portfolios, and provide AI-driven investment insights using transformer neural network models. Additionally, it incorporates machine learning pipeline to analyze financial statements,  assess company sentiments and predict stock prices. Meta Llama 3 will be used as Large Language Model (LLM) with a local Ollama server to run a sentiment analysis of recent financial new headlines scraped from the web using the News API. 

## Features and pages
- **Homepage**: daily/weekly/monthly/yearly/ytd stock price changes, total gains/losses
- **AI Stock Analyser Chatbot**: Use a Large Language Model (Mistal 7b) to predict stock prices. Will use advanced quantitative tools for evaluating options, derivatives, and hedging strategies.
- **Watchlist**: Add stocks to watchlist and track their performance. Receive alerts on significant market movements and stock price changes.
- **Portfolio**: Track and manage your investment portfolio. AI-driven analysis of portfolio risk and diversification.
- **Economic Calendar**: View upcoming economic events and their impact on the market.
- **Stock Screener**: Filter stocks based on user-defined criteria. AI will analyse the company's financial statements and provide insights on fundamentals and sentiment.
- **News Feed**: Receive relevant news based on the stocks in the user's portfolio and watchlist.

To come:
- **Deep Learning Analysis**:
  - Evaluate financial statements for insights into company performance.
  - Perform sentiment analysis on company-related news and reports.


## Tech Stack
- **Backend**: Python
- **APIs & Data Sources**:
  - yFinance API (Real-time stock data)
  - News API (Financial news updates)
  - Mistral API with open-mitral-7b model (Investment advisory)
  - SimFin API (Financial statement data)
- **Deep Learning & Machine Learning Frameworks**:
  - TensorFlow/PyTorch (Financial statement analysis)
  - NLP Models (Sentiment analysis, market news processing)
  - Scikit-Learn (Stock prediction models, quantitative finance calculations)
  - this will be on Google Colab at first, then migrated to Ollama3 local server
- **Frontend**: Streamlit (UI Framework)
- **Database**: Firestore (Cloud Firestore for user data & portfolio storage)
- **Deployment**: Railway.app

Sources:
- SimFin API: https://simfin.readme.io/reference/getting-started-1