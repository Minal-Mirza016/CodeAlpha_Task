import yfinance as yf
import pandas as pd
import numpy as np

# Function to fetch the current price of a stock
def get_current_price(ticker):

    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="1d")
        if not history.empty:
            return history['Close'].iloc[0]
        else:
            raise ValueError(f"{ticker}: Possibly delisted or no price data found.")
    except Exception as e:

        print(f"Error fetching price for {ticker}: {e}")
        print(f"${ticker}: possibly delisted; no price data found (Yahoo error = '{str(e)}')")
        return np.nan


def add_stock(portfolio):

    try:

        ticker = input("Enter stock ticker: ").strip().upper()
        shares = float(input("Enter number of shares (positive number): "))
        purchase_price = float(input("Enter purchase price per share (positive number): "))

        if shares <= 0 or purchase_price <= 0:
            raise ValueError("Shares and purchase price must be positive numbers.")

        portfolio.append({"Ticker": ticker, "Shares": shares, "Purchase Price": purchase_price})
        print(f"Added {ticker} to the portfolio.")
    except ValueError as e:

        print(f"Error: {e}. Please try again.")

# Function to display the stock portfolio
def display_portfolio(portfolio):

    if not portfolio:
        print("Your portfolio is empty!")
        return

    data = []
    for stock in portfolio:
        ticker = stock['Ticker']
        shares = stock['Shares']
        purchase_price = stock['Purchase Price']
        current_price = get_current_price(ticker)

        # Calculate values
        invested = shares * purchase_price
        if not np.isnan(current_price):
            current_value = shares * current_price
            gain_loss = current_value - invested
        else:
            current_value = np.nan
            gain_loss = np.nan

        # Add details to the data list
        data.append([ticker, shares, purchase_price,
                     current_price if not np.isnan(current_price) else "N/A",
                     invested,
                     current_value if not np.isnan(current_value) else "N/A",
                     gain_loss if not np.isnan(gain_loss) else "N/A"])

    # Convert data to a DataFrame for better visualization
    df = pd.DataFrame(data, columns=["Ticker", "Shares", "Purchase Price", "Current Price", "Invested", "Current Value",
                                     "Gain/Loss"])


    print("\nPortfolio Summary:")
    print(df.to_string(index=False))


    total_gain_loss = df["Gain/Loss"]
    if total_gain_loss.dtype != "O":
        total_gain_loss = total_gain_loss.sum(skipna=True)
        print(f"\nTotal Portfolio Gain/Loss: ${total_gain_loss:.2f}")
    else:
        print("\nTotal Portfolio Gain/Loss: Unable to calculate due to missing data.")


def main():

    portfolio = []
    while True:

        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")
        # Get user choice
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_stock(portfolio)
        elif choice == "2":
            display_portfolio(portfolio)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
