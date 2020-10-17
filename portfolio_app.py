import portfolio_functions as fun
import streamlit as st
import pandas as pd
import numpy as np
# import scipy.optimize as sco
# import yfinance as yf
import matplotlib.pyplot as plt
# pylint: disable=no-member

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                    content:'*P.S. This application is suggestive at best. Please invest at your own discretion *';
                    visibility: visible;
                    display: block;
                    position: relative;
                    # background-color: red;
                    padding: 5px;
                    top: 2px;
                }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


@st.cache()
def comp_list():
    companies = pd.read_table(
        'http://ftp.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt', sep='|', index_col=False)
    # https://quant.stackexchange.com/questions/1640/where-to-download-list-of-all-common-stocks-traded-on-nyse-nasdaq-and-amex
    companies.drop(companies.tail(1).index, inplace=True)  # drop last n rows
    for i in range(len(companies)):
        if '-' in companies.loc[i]['Security Name']:
            companies.at[i, 'Security Name'] = (
                companies.loc[i]['Security Name'].rpartition('-'))[0]
    companies['symbol_name'] = companies['Symbol'] + \
        '-' + companies['Security Name']
    return companies['symbol_name']


@st.cache()
def start():
    a = 1
    return a


a = start()
st.title('Portfolio Optimization')

# st.sidebar.header('Your Portfolio Investment')
st.write("""         
         Portfolio Management is the process of maximizing the return on a portfolio. 
         While managing a portfolio we should aim at minimizing the risk and maximize returns. 

         """)


st.sidebar.info(
    'This app helps you analyse which stocks can be worthy of investment for an ameture stock enthusiast.')
st.header('Your Portfolio')
st.write('Please enter the information below')
comp_list = comp_list()

port_list = st.multiselect('Companies in your portfolio',
                           comp_list,
                           )

num_portfolios = 50000


st.sidebar.write('Please enter the information below')
num_portfolios = st.sidebar.number_input(
    'Money to Invest', value=num_portfolios)

# num_portfolios = st.slider('Money to Invest', 0, 100000, num_portfolios)

df = fun.comp_details(port_list)
# st.write(port_list)

# st.write(num_portfolios)

if len(port_list) >= 1:
    a = 3


if a > 2:
    mean_returns = df.pct_change().mean()
    cov = df.pct_change().cov()
    rf = fun.risk_free(port_list)
    optimal_port_sharpe = fun.max_sharpe_ratio(mean_returns, cov, rf)
    results = pd.DataFrame([round(x, 2)
                            for x in optimal_port_sharpe['x']], index=port_list).T
    results = results.reindex(sorted(results.columns), axis=1)

    st.subheader('Optimized Portfolio')
    st.write('''The table below provides the proportion of stock investments that are to be made in an optimized portfolio.
                The bar chart below provides the proportions in terms of your initial investment amount.    ''')
    st.write(results)

    results = results*num_portfolios
    # st.bar_chart(results.T)
    plt.style.use('ggplot')
    fig = plt.figure()
    # creating the bar plot
    plt.bar(list(results.columns), [float(x) for x in results.values.T], color='maroon',
            width=0.4)
    # plt.xlabel("Portfolio")
    plt.ylabel("Price to invest")
    # plt.title("Optimized Portfolio")
    plt.xticks(rotation=80)
    plt.show()
    st.pyplot(fig)

    st.write("""
            
            Portfolio weights that would match the “optimal” means the portfolio with the highest Sharpe ratio, 
            also known as the “mean-variance optimal” portfolio. Aim is to optimise a portfolio of stocks based on 
            minimising the cost function of negative Sharpie ratio. 
            
            We try to discover the optimal weights by creating many random portfolios, all with varying randomly weights,
            calculating and recording the Sharpe ratio of each of these and then finally extracting the details 
            corresponding to the result with the highest value.

            """)

    st.subheader('Correlation Plot')
    st.write('''
        We use heat maps to visualize the correlation ranges among the competing stocks.
                Blue and lighter shades are directly proportional to higher correlation, which may
                indicate dependancies.
                ''')
    retscomp = df.pct_change()
    corr = retscomp.corr()
    plt.style.use('classic')
    fig = plt.figure()
    plt.imshow(corr, cmap='RdBu', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns)
    plt.yticks(range(len(corr)), corr.columns)
    st.pyplot(fig)

    st.subheader('Best Performing equity in the Portfolio')
    best = results.eq(results.max(1), axis=0).dot(results.columns)
    best_name = (list(best.values)[0].rpartition('-'))[0]
    fig = plt.figure()
    plt.plot(df[best_name])
    plt.title("Closing Price Line Chart of " + best[0])
    st.pyplot(fig)
    # st.line_chart(df[best])
    st.write('''
        Time series forecasting can be performed on the best performing equity to perform futher analysis. 
        Due to limitation on the hosting platform, we cannot perform it in real-time. For more information on how to
        implement LSTMS for time series analysis visit [link](http://bit.ly/git_finance)

    ''')

st.sidebar.write(
    "This based on the "
    "[**project**](http://bit.ly/git_finance) "
    "developed by [**Akhil Sanjay Potdar**](http://bit.ly/profileakhil). Enjoy!\n\n"
)

# st.write(
#     '*P.S. This application is suggestive at best. Please invest at your own discretion *')
