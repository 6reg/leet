"""
This program takes a list of numbers and returns the difference between the biggest and smallest number.

pseudocode:
    high = 0
    low = prices[i]
    max_diff = high - low
    for price in prices:
        if price is < low
            low = price
    high = max(prices)
    return high - low
"""

def max_profit(prices):
    high = 0
    for price in range(len(prices)):
        low = min(prices)
        high = max(prices)
        mp = high - low
    return mp

print(max_profit([1,2,3,4, 6, 7]))
