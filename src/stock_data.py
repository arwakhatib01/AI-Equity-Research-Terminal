import pandas as pd
import yfinance as yf
def download_company_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    company_info = ticker.info
    price_history = ticker.history(period="5y")
    price_history.to_csv("data/raw/price_history.csv")
    income_statement = ticker.financials
    income_statement.to_csv("data/raw/income_statement.csv")
    balance_sheet = ticker.balance_sheet
    balance_sheet.to_csv("data/raw/balance_sheet.csv")
    cash_flow = ticker.cashflow
    cash_flow.to_csv("data/raw/cash_flow.csv")
    print("Data downloaded successfully!")
    
    