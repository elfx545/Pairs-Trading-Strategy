"""
    Title: Buy and Hold (NYSE)
    Description: This is a long only strategy which rebalances the 
        portfolio weights every month at month start.
    Style tags: Systematic
    Asset class: Equities, Futures, ETFs, Currencies and Commodities
    Dataset: US Equities
"""
from blueshift.api import (
    symbol,
    order_target_percent,
    schedule_function,
    date_rules,
    time_rules,
    record,
)
import numpy as np

def initialize(context):
    schedule_function(
        check_pairs, 
        date_rules.every_day(), 
        time_rules.market_close(minutes=0, hours=1)
    )
    
    # Test avec Coca-Cola (KO) et PepsiCo (PEP)
    context.ko = symbol("KO")
    context.pep = symbol("PEP")

    context.long_on_spread = False
    context.shorting_spread = False

def check_pairs(context, data):
    ko = context.ko
    pep = context.pep

    prices = data.history([ko, pep], 'close', 30, '1d')
    short_prices = prices.iloc[-1:]

    # Calcul du Spread (KO - PEP)
    mavg_30 = np.mean(prices[ko] - prices[pep])
    std_30 = np.std(prices[ko] - prices[pep]) 

    mavg_1 = np.mean(short_prices[ko] - short_prices[pep])

    if std_30 > 0:
        zscore = (mavg_1 - mavg_30) / std_30

        if zscore > 1.0 and not context.shorting_spread:
            order_target_percent(ko, -0.5)
            order_target_percent(pep, 0.5)
            context.shorting_spread = True
            context.long_on_spread = False

        elif zscore < -1.0 and not context.long_on_spread:
            order_target_percent(ko, 0.5)
            order_target_percent(pep, -0.5)
            context.shorting_spread = False
            context.long_on_spread = True        

        elif abs(zscore) < 0.1:
            order_target_percent(ko, 0)
            order_target_percent(pep, 0)
            context.shorting_spread = False
            context.long_on_spread = False 

        record(z_score=zscore)