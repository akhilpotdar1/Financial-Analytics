import streamlit as st
import pandas as pd
import numpy as np
import scipy.optimize as sco
import yfinance as yf


def calc_neg_sharpe(weights, mean_returns, cov, rf):
    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_std = np.sqrt(
        np.dot(weights.T, np.dot(cov, weights))) * np.sqrt(252)
    sharpe_ratio = (portfolio_return - rf) / portfolio_std
    return -sharpe_ratio


constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})


def max_sharpe_ratio(mean_returns, cov, rf):
    num_assets = len(mean_returns)
    args = (mean_returns, cov, rf)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bound = (0.0, 1.0)
    bounds = tuple(bound for asset in range(num_assets))
    result = sco.minimize(calc_neg_sharpe, num_assets*[1./num_assets, ], args=args,
                          method='SLSQP', bounds=bounds, constraints=constraints)
    return result

# get data on the ticker


def risk_free(port_list):
    num = st.sidebar.number_input('Number of Risk Free Assets', min_value=0,
                                  max_value=len(port_list), value=0, step=1)
    return num


def comp_details(port_list):
    names = [(port_list[i].rpartition('-'))[0] for i in range(len(port_list))]
    # name='AAPL'

    def get_price(name):
        df = yf.Ticker(name)
        close_price = df.history(period='20y')['Close']
        return(close_price.values)
    d = {str(i): get_price(i) for i in names}
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in d.items()]))
    return(df)
