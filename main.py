import openpyxl
import os
import pandas as pd
file = "Income by Country.xlsx"
sheets = pd.ExcelFile(file).sheet_names

for sheet in sheets:
    df = pd.read_excel(file,sheet_name=sheet)
    csv = sheet + ".csv"
    df.to_csv(csv,index=False)
