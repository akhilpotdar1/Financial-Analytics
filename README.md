
# [Financial Analytics](https://portfolio-opt-app.herokuapp.com/)

The deployed web app is live at https://portfolio-opt-app.herokuapp.com/

## Introduction
In this project we attempt to perform portfolio price prediction using neural networks (LSTM)
along with optimization using Monte Carlo and Scipy optimizers. This project aims to be tool for
an amateur stock trader to use in his/her trading or investment activities. A diversified portfolio
of 5 stocks 2 tech companies (Alphabet, Tesla), 2 mutual funds (Vanguard 500, SAP 500) and 1
non-traditional fund (water stocks i.e American Water Works) is used to demonstrate the use of
these tools. We will be checking the forecasts of these stocks to identify trends and take
calculative decisions whether to invest further based on various factors such as risk, growth,
stability and so forth.

This project is divided in two parts. Part 1 focuses of stock price prediction using Neural
Networks and Part 2 focuses of portfolio optimization. 

## Video Explaining the project
https://www.youtube.com/watch?v=YIsVBKGLiT0&t=2s

## Dataset
Stock price data was from Yahoo Finance. 5 stocks 2 tech companies (Alphabet, Tesla), 2 mutual
funds (Vanguard 500, SAP 500) and 1 water stocks i.e American Water Works. 5 yrs data from
2014 till date is taken for analysis. There are multiple variables in the dataset – date, open, high,
low, close and Volume
• The columns Open and Close represent the starting and final price at which the stock is
traded on a day.
• High, Low represent the maximum, minimum of the share for the day.
• Volume is the number of shares bought or sold in the day

## Links used for scripting
https://towardsdatascience.com/predicting-stock-price-with-lstm-13af86a74944
https://www.analyticsvidhya.com/blog/2018/10/predicting-stock-price-machine-learningnd-deep-learning-techniques-python/
https://medium.com/sfu-big-data/predicting-stable-portfolios-using-machine-learning-f2e27d6dbbec
https://pythonforfinance.net/2019/07/02/investment-portfolio-optimisation-with-python-revisited/
https://www.datacamp.com/community/tutorials/lstm-python-stock-market?source=post_page---------------------------
https://towardsdatascience.com/in-12-minutes-stocks-analysis-with-pandas-and-scikit-learn-a8d8a7b50ee7
https://towardsdatascience.com/efficient-frontier-portfolio-optimisation-in-python-e7844051e7f

## Conclusions
As seen through the results in this project, the user of these tools gets a fair picture of his/her investments
in the stock market. Through the above examples we see that a non-traditional stock i.e water
stock (AWK) has a higher weight in the optimized portfolio and that the Vangaurd 500 mutual
funds can also be a good investment choice. While the results state that investment in Tesla can
be a bad in the long run, one must also consider sentiment analysis which has not been included
in this project. Furthermore, the LSTM models can also help a client analyze his portfolio for
trading practices, however with caution as even till date, no machine learning model can
correctly predict all the price movements all the time. With the other tools at disposal the trader
can also include this for further validity into his practices.

As such the prediction and optimization of a portfolio of 5 stocks helps the user get insights to
take calculative decisions whether to invest further based on various factors such as risk, growth,
stability. Having had said that, one must always follow his instincts upon reading of the various
information available and only then take a stand.
