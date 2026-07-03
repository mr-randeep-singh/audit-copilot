import os
from dotenv import load_dotenv
from edgar import set_identity, Company

load_dotenv()                                  # reads .env into environment
set_identity(os.environ["EDGAR_IDENTITY"])     # tells EDGAR who you are

company = Company("XOM")                       # ExxonMobil, by ticker
filings = company.get_filings(form="10-K")
print("Latest 10-K:", filings[0].filing_date)