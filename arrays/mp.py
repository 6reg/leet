def max_profit(prices):
    # Initially the lowest price would be the first price in the given array
    
    lowest_price = prices[0] # accessing the first element from the given array

    # And profit would be zero
    profit = 0

    # Now as we've accessed the first element from the given jarray we'll loop from the 2nd
    for i in range(1, len(prices)): # looping from 2nd element up to the last element in the array
            # check if current price is smaller than the lowest_price
        if prices[i] < lowest_price:
            # if yes then make current price lowest since it's new lowest price in given array
            lowest_price = prices[i]
        else: # if not check if it maximizes the profit
            profit = max(profit, prices[i] - lowest_price) # compare both vales 
    return profit

print(max_profit([1,2,3,4,5]))
         
