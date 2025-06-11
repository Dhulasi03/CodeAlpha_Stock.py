# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

portfolio = {}  # To store stock and investment value
total_investment = 0

print("Stock Portfolio Tracker")
print("Enter your stock holdings.")
print("Type 'done' when you are finished.\n")

while True:
    stock = input("Enter stock name (e.g., AAPL): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found in our database. Please try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Invalid quantity. Please enter a valid number.\n")
        continue

    investment = stock_prices[stock] * quantity
    portfolio[stock] = investment
    total_investment += investment

    print(f"Added {quantity} shares of {stock} worth ₹{investment}\n")

# Display the portfolio summary
print("\nPortfolio Summary:")
for stock, value in portfolio.items():
    print(f"{stock}: ₹{value}")

print(f"\nTotal Investment: ₹{total_investment}")

# Save the result to a text file (with UTF-8 encoding)
with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, value in portfolio.items():
        file.write(f"{stock}: ₹{value}\n")
    file.write(f"\nTotal Investment: ₹{total_investment}")
