from src.data.stock_data import download_company_data

print("=" * 60)
print("AI EQUITY RESEARCH TERMINAL")
print("=" * 60)

ticker = input("Enter Company Ticker: ")

download_company_data(ticker)