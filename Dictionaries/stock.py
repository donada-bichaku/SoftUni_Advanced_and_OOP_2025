stock_data = input().split()
stock = {}

for i in range(0, len(stock_data), 2):
    key = stock_data[i]
    value = stock_data[i+1]
    stock[key] = value

product_to_search = input().split()

for product in product_to_search:
    if product in stock:
        print(f"we have {stock[product]} {product}")
    else:
        print(f"sorry, no {product}")
