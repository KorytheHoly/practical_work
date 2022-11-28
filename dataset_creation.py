import yfinance as yf
import pandas as pd
data = yf.download("MSFT", start="2017-01-01", end="2017-04-30")
df = pd.DataFrame(data)
print(df)
