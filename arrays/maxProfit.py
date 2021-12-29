def maxProfit(prices):
    max_profit, min_price = 0, prices[0]

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

print(maxProfit([2,5,8,9]))
