from datetime import date
from datetime import timedelta

import pandas
import yfinance

keys = [
    'currentPrice',
    'targetLowPrice',
    'targetMedianPrice',
    'targetMeanPrice',
    'targetHighPrice',
    'numberOfAnalystOpinions',
    'recommendationKey',
    'recommendationMean',
    'totalCash',
    'totalDebt',
    'totalRevenue',
    'exchange',
    'shortName',
    'forwardPE',
    'pegRatio'
]


def get_history(portfolio: []) -> pandas.DataFrame:
    quotes : pandas.DataFrame
    symbols = []
    for asset in portfolio:
        symbols.append(asset['symbol'])

    today = date.today().strftime('%Y-%m-%d')
    start = (date.today() - timedelta(90)).strftime('%Y-%m-%d')
    quotes = yfinance.download(' '.join(symbols), start=start, end=today, group_by='tickers')
    return quotes

def get_info(portfolio:[]) -> {}:
    all_info = {}
    symbols = []
    for asset in portfolio:
        symbols.append(asset['symbol'])
    tickers = yfinance.Tickers(','.join(symbols))
    for symbol in symbols:
        sym_info = {}
        y_info = tickers.tickers[symbol.upper()].info
        for key in y_info.keys():
            sym_info[key] = y_info[key]
        all_info[symbol] = sym_info
    return all_info


def get_quote(symbol) -> {}:
    result = {}
    quote = yfinance.Ticker(symbol)
    info = quote.info
    for key in keys:
        result[key] = info[key]

    return result
