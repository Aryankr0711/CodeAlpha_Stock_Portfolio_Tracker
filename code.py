import requests
import json

# Replace with your Alpha Vantage API key
API_KEY = 'YOUR_API_KEY_HERE'
USD_TO_INR_RATE = 75  # Exchange rate from USD to INR

# Function to fetch real-time stock data
def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']
    else:
        print(f"Failed to fetch data for {symbol}: {data}")
        return None

# Function to add a stock to the portfolio
def add_stock(portfolio, symbol, shares):
    stock_data = get_stock_data(symbol)
    if stock_data:
        price_inr = float(stock_data['05. price']) * USD_TO_INR_RATE
        portfolio[symbol] = {
            'shares': shares,
            'price': price_inr
        }
        print(f"{symbol} added to portfolio with price ₹{price_inr:.2f}.")
    else:
        print(f"Failed to add {symbol} to portfolio.")

# Function to remove a stock from the portfolio
def remove_stock(portfolio, symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")

# Function to calculate the total portfolio value
def calculate_portfolio_value(portfolio):
    total_value = 0.0
    for symbol, data in portfolio.items():
        stock_data = get_stock_data(symbol)
        if stock_data:
            current_price_inr = float(stock_data['05. price']) * USD_TO_INR_RATE
            total_value += current_price_inr * data['shares']
            print(f"Current price of {symbol} in INR: ₹{current_price_inr:.2f}")
        else:
            print(f"Failed to fetch current price for {symbol}.")
    return total_value

# Example usage
if __name__ == "__main__":
    portfolio = {}

    # Adding stocks to the portfolio
    add_stock(portfolio, 'TSLA', 5)
    add_stock(portfolio, 'MSFT', 10)

    # Displaying current portfolio
    print("Current Portfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['shares']} shares at ₹{data['price']:.2f} each")

    # Calculating total portfolio value
    total_value = calculate_portfolio_value(portfolio)
    print(f"Total Portfolio Value: ₹{total_value:.2f}")

    # Removing a stock from the portfolio
    remove_stock(portfolio, 'MSFT')

    # Displaying updated portfolio
    print("Updated Portfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['shares']} shares at ₹{data['price']:.2f} each")

    # Calculating total portfolio value again
    total_value = calculate_portfolio_value(portfolio)
    print(f"Total Portfolio Value: ₹{total_value:.2f}")
