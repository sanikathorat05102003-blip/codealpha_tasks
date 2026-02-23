# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0
investment_details = []

print("Simple Stock Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))
    value = stock_prices[stock] * quantity
    total_investment += value

    investment_details.append(f"{stock} - {quantity} shares - ${value}")
    print(f"Added: {stock}, Investment Value = ${value}")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save to file
with open("investment.txt", "w") as file:
    for item in investment_details:
        file.write(item + "\n")
    file.write(f"\nTotal Investment: ${total_investment}")

print("Investment details saved to investment.txt")

