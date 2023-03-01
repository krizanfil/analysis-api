from typing import Dict
from analysis import graham, pabrai
import yfinance as yf

analyses_result = Dict[str, float]


def process_ticker_data(info: Dict, fast_info: Dict) -> analyses_result:
    """
    Function that gets and processes the data received from yahoo finance.
    :param info: Dict[str, Optional[int]]
    :param fast_info: Dict[str, Optional[int]]
    :return: Dict[str, float]
    """
    data = {
        'fcf': info.get('freeCashflow'),
        'growth_rate': info.get('revenueGrowth'),
        'market_cap': fast_info.get('market_cap'),
        'excess_capital': info.get('totalCash'),
        'eps': info.get("trailingEps"),
        'bvps': info.get("bookValue")
    }

    for key, value in data.items():
        if not value:
            data[key] = 0
        if key in ['fcf', 'market_cap', 'excess_capital']:
            data[key] /= 1000000000

    data['sector'] = info.get('sector')

    return data


def process_ticker(ticker: str) -> analyses_result:
    yf_ticker = yf.Ticker(ticker)
    info, fast_info = yf_ticker.info, yf_ticker.fast_info
    data = process_ticker_data(info, fast_info)

    result = {
        ticker: f'Graham result is {graham(data)}, DCF result is {pabrai(data)}'
    }

    return result
