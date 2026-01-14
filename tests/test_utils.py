import pytest
import pandas as pd
import numpy as np
from src.utils.black_scholes import bs_gamma
from src.utils.gex import row_gross_gex, apply_dealer_sign

def test_bs_gamma():
    # ATM option: S=100, K=100, T=1, sigma=0.2
    # Gamma should be approx 0.0199 (1 / (100 * 0.2 * 1) * 0.3989)
    # N'(0) = 0.3989
    gamma = bs_gamma(s=100, k=100, t=1.0, sigma=0.2)
    assert 0.019 < gamma < 0.021

    # Deep OTM option should have near zero gamma
    gamma_otm = bs_gamma(s=100, k=200, t=1.0, sigma=0.2)
    assert gamma_otm < 0.0001

def test_row_gross_gex():
    # Setup a dummy dataframe row
    data = {
        "gamma": [0.05],
        "open_interest": [1000],
    }
    df = pd.DataFrame(data)
    spot = 100
    multiplier = 100
    gamma_scale = 0.01
    
    # Calculation: gamma * OI * spot^2 * multiplier * scale
    # 0.05 * 1000 * 10000 * 100 * 0.01
    # 50 * 10000 * 1 = 500,000
    
    result = row_gross_gex(df, spot, multiplier, gamma_scale)
    assert result.iloc[0] == 500000.0

def test_apply_dealer_sign():
    assert apply_dealer_sign(100, dealer_short=True) == -100
    assert apply_dealer_sign(100, dealer_short=False) == 100
