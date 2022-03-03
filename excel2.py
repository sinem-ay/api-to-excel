# Api-to-excel but for only one time??
# Crypto API to Excel
# Source:

import pandas as pd

df = pd.read_csv("https://data.messari.io/api/v1/assets/btc/metrics")

writer = pd.ExcelWriter('crypto.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()