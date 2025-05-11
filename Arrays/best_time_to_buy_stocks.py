def max_profit(prices):
    # Initialize min_price to infinity, so any price will be smaller initially
    min_price = float('inf')

    # Initialize max_profit to 0, as no profit is made at the start
    max_profit = 0

    # Loop through each price in the prices list
    for price in prices:
        # If the current price is less than the current min_price, update min_price
        if price < min_price:
            min_price = price

        # If the current profit (price - min_price) is greater than the max_profit, update max_profit
        elif price - min_price > max_profit:
            max_profit = price - min_price

    # Return the maximum profit found
    return max_profit


print(max_profit([7, 1, 5, 3, 6, 4]))
