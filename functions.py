import numpy as np
import pandas as pd


def call_option_value(strike: float, premium: float, spot: float, buy: bool) -> float:
    if buy:
        return max(spot - strike, 0) - premium
    else:
        return premium - max(spot - strike, 0)
    

def put_option_value(strike: float, premium: float, spot: float, buy: bool) -> float:
    if buy:
        return max(strike - spot, 0) - premium
    else:
        return premium - max(strike - spot, 0)


def premium_spread(strike: float, premium: float, buy: bool, call: bool) -> pd.DataFrame:
    x, y = [], []
    for i in range(int(strike * 100) - 5000, int(strike * 100) + 5000, 5):
        x.append(i / 100)
        if call:
            y.append(call_option_value(strike, premium, i / 100, buy))
        else:
            y.append(put_option_value(strike, premium, i / 100, buy))

    return pd.DataFrame({'Spot': x, 'Value': y})

