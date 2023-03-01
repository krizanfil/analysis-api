from typing import Dict, Optional
import numpy as np


def graham(
        data: Dict[str, float],
        discount_rate: float = 0.3
) -> float:
    """
    Takes data about a stock in form of a dict and runs Benjamin Graham's stock analyses model on
    it and returns how many bagger it is. (intrinsic value with a proper discount rate)
    :return: float
    """
    eps, bvps = data['eps'], data['bvps']

    if not eps or not bvps:
        return -1

    if eps < 0 or bvps < 0:
        return -1

    graham_number = np.sqrt(22.5 * eps * bvps)

    return graham_number / (1 + discount_rate)


def pabrai(
    data: Dict[str, float],
    discount_rate: Optional[float] = 0.3,
    years: Optional[int] = 10
) -> float:
    """
    Takes data about a stock in form of a dict and runs discounted cash flow stock analyses model on
    it and returns how many bagger it is. (Intrinsic evaluation of the company divided by its
    current market cap.) In case of core information about the stock is missing return -1, in case
    of missing growth rate uses growth rate equal to 0.
    :return: float
    """
    fcf, growth_rate = data['fcf'], data['growth_rate'] + 1
    market_cap, excess_capital = data['market_cap'], data['excess_capital']

    if not (fcf and market_cap):
        return -1

    if not growth_rate:
        growth_rate = 0

    total_fcf = 0
    for _ in range(1, years + 1):
        fcf *= growth_rate
        total_fcf += fcf

    intrinsic_value = total_fcf / (1 + discount_rate) ** years + excess_capital

    return intrinsic_value / market_cap
