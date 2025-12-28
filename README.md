# 📈 Algo-Trader: Quantitative Trading Strategy Backtester

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Finance](https://img.shields.io/badge/Domain-Fintech-green) ![Status](https://img.shields.io/badge/Status-Active-success)

Algo-Trader is an automated trading simulation engine designed to backtest technical analysis strategies on real-world market data (Stocks & Crypto).

## 🚀 Project Overview

Manual trading is emotional and prone to errors. This project solves that by automating the decision-making process using the **Golden Cross Strategy**. It processes historical data to evaluate how profitable a strategy would have been if executed by a robot.

**Key Features:**
* **Real-time Data Fetching**: Integrates with Yahoo Finance API (`yfinance`) to get live/historical prices for Bitcoin (BTC), Ethereum (ETH), or any Stock (e.g., AAPL, BBCA).
* **Technical Analysis Engine**: Automatically calculates Simple Moving Averages (SMA 20 & SMA 50).
* **Strategy Backtesting**: Simulates "Buy" and "Sell" orders based on algorithm logic over a 2-year period.
* **Performance Metrics**: Calculates Total Profit, ROI (Return on Investment), and Win Rate.
* **Visual Reporting**: Generates a matplotlib chart pinpointing exact entry and exit points.

## 🧠 The Strategy: "Golden Cross"

The bot follows a classic trend-following strategy:
1.  **Golden Cross (BUY Signal 🟢)**: When the short-term trend (SMA 20) crosses *above* the long-term trend (SMA 50). This indicates upward momentum.
2.  **Death Cross (SELL Signal 🔴)**: When the short-term trend (SMA 20) crosses *below* the long-term trend (SMA 50). This indicates a potential crash.

## 🛠️ Technology Stack

* **Python**: Core logic.
* **Pandas**: Time-series data manipulation and rolling window calculations.
* **Yfinance**: Financial market data API.
* **Matplotlib**: Data visualization for trade mapping.

## 📊 Sample Result (Simulation on BTC-USD)

```text
========================================
HASIL AKHIR TRADING BOT (BTC-USD)
========================================
Modal Awal      : Rp 10,000,000
Saldo Akhir     : Rp 18,450,000
Total Profit    : Rp 8,450,000 (84.50%)
Total Transaksi : 12 (Win: 8 | Loss: 4)
Win Rate        : 66.67%
Vs Buy & Hold   : 55.20%
========================================
