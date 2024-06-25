stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
    print(stock_prices[x-1])

def max_price(a, b):
    print(max(stock_prices[(a - 1): (b - 1)]))

def min_price(a, b):
    print(min(stock_prices[(a - 1) : (b - 1)]))

price_at(4)
max_price(3, 6)
min_price(12, 18)