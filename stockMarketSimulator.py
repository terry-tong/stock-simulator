#Stock Data Source
import yfinance as yf

class User:
    def __init__(self):
        self.portfolio = []
        self.cash = int(input("Enter starting amount: "))

    def __str__(self):
        print(self.portfolio)
        print(self.cash)
        return 0

    def buy(self):
        ticker = str(input("Enter ticker of stock you'd like to buy: "))
        tickerData = yf.Ticker(ticker).info["regularMarketPrice"]
        amount = int(input("Enter amount to buy: "))
        self.portfolio.append([ticker,amount])
        self.cash -= tickerData * amount

    def sell(self):
        ticker = str(input("Enter ticker of stock you'd like to buy: "))
        amount = int(input("Enter amount to buy: "))


terry = User()
terry.buy()
print(terry)