## Table of Contents

1. [Problem Description](#problem-description)
2. [Data Sources](#data-sources)
3. [Data Transformations + EDA](#data-transformations-eda)
4. [Modeling](#modeling)
5. [Trading Simulation](#trading-simulation)
6. [Automation](#automation)
7. [Bonus Points](#bonus-points) 

## Problem Description 
(1 point) Problem is described in README briefly without much detail.

(1 point) Problem is described in README with enough context and the end goal, so it is clear what the problem is and how the solution will be used.

(1 point) New problem definition (not just the current setup of a week-long strategy for the largest stocks): e.g., hourly or long-term trading for stocks, different stock exchanges (other countries), crypto, betting, etc.

(1 point) State-of-the-art clear description of each step, findings, and how to reproduce it. It is easy to understand the logic of each step, and important findings/difficulties are outlined.

## Data Sources 
(1 point) Use the data sources and the features from the lectures.

(1 point) 20+ new features with their description in the data sources section (+10% volume).

(1 point) New datasource is introduced - not YFinance, Fred (e.g., paid data, web scraping, alternative free data provider with unique features, etc.).

(1 point) Large dataset with >1 million of records.

## Data Transformation
(1 point) Data is combined into one data frame. Feature sets are defined (TO_PREDICT, NUMERIC, DUMMIES, etc.).

(1 point) New relevant features are generated from transformations (at least 5. One dummy set is one feature): it can be binned variables from numeric features or manual transformations.

(1 point) Exploratory Data Analysis: describe variables you want to predict, run correlation analysis between features and TO_PREDICT, etc.

## Modeling
(1 point) One model from the lecture is used (DecisionTree, RandomForest).

(1 point) More than one model from the lecture is used to generate predictions.

(1 point) Custom decision rules on target higher probability events.

(1 point) Hyperparameters tuning is used to tune models.

(1 point) New models are introduced: XGBoost, Regression, Deep Neural Networks and their variations (RNN, LSTM, GNN).

## Trading Simulation
(1 point) Vector simulations for at least 1 strategy (and approximate returns on capital).

(1 point) Two or more strategies are covered (sim1_, sim2_, etc. fields are generated for each prediction).

(1 point) Exact simulations (iter.rows) with reinvestment of capital gains and efficient capital utilization.

(1 point) Profitability discussion vs. benchmark, CAGR, Sharpe ratio, max drawdown, rolling returns, etc.

(1 point) The best strategy has advanced features: risk management (e.g., stop loss), time of entry/sell, increased investment with higher probability, portfolio optimization.

(1 point) New strategy: introduce a new empirical strategy based on the predictions, e.g., long-short strategy, or use no more than 1-3-5 concurrent investments, or combine with market conditions (trade only when volatility is high or current price is close to 52 weeks low), etc.

(1 point) Exceptional profitability: choose a realistic benchmark (e.g., S&P500 index) and show that your best prediction/strategy delivers better performance (CAGR) on average than a benchmark.

(1 point) Deep exploratory analysis: how predictions/precision are different by tickers (or markets, or month of year, or other features, etc.). Debug wrong predictions. Give ideas on the data features/models/strategies improvement based on the insights.

## Automation
(1 point) All notebooks (used in workflow) are exported to scripts. There is one notebook that calls all functions from the .py files and shows how to execute the workflow (end-to-end data workflow: download, transform, predict, simulate, show the latest new trades).

(1 point) Dependencies are managed (e.g., file with dependencies, pipfile + README explaining how to install dependencies and activate the environment).

(1 point) The full system can be re-run via Cron job and generate predictions for the last available data (e.g., last day data -> predictions for the future days).

(1 point) Two regimes for the system: run from a file on drive (easy to replicate, no data loading+transformations, but no update for the latest data), or download data from the sources.

(1 point) Incremental data loading/transformations with storage on drive/database/elsewhere (not on GitHub).

## Bonus Points
(1 point) The code is well designed and commented on in modules.

(1 point) Additional code to place bets through any Brokers API.

(1 point) Additional code for monitoring models, financial results, trades → e.g., a dashboard (describe how to make it live), or Telegram bot to send messages with trades, data updates, etc.

(1 point) Containerization.

(1 point) Cloud deployment.

(1-2 points) Subjective bonus points from a peer reviewer: why do you like the project, what was particularly well done in the project?