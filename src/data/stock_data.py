import json

import pandas as pd
import yfinance as yf

from config import RAW_DATA_DIR
from src.utils.logger import logger


def download_company_data(ticker_symbol):
    """
    Downloads company financial data from Yahoo Finance.
    """

    ticker_symbol = ticker_symbol.upper()

    logger.info(f"Downloading data for {ticker_symbol}")

    ticker = yf.Ticker(ticker_symbol)

    company_folder = RAW_DATA_DIR / ticker_symbol
    company_folder.mkdir(parents=True, exist_ok=True)

    company_info = ticker.info

    price_history = ticker.history(period="5y")

    income_statement = ticker.financials

    balance_sheet = ticker.balance_sheet

    cash_flow = ticker.cashflow

    print("=" * 60)
    print(company_info.get("longName", "Unknown Company"))
    print("=" * 60)

    with open(company_folder / "company_info.json", "w") as file:
        json.dump(company_info, file, indent=4)

    price_history.to_csv(company_folder / "price_history.csv")

    income_statement.to_csv(company_folder / "income_statement.csv")

    balance_sheet.to_csv(company_folder / "balance_sheet.csv")

    cash_flow.to_csv(company_folder / "cash_flow.csv")

    logger.info(f"Finished downloading {ticker_symbol}")

    print("\nDownload Complete!")
    print(company_folder)