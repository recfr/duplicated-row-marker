import pandas as pd
import openpyxl

excel_file = "input_isDuplicated.xlsx"
df = pd.read_excel(excel_file, sheet_name='Sheet1')

duplicateRowsDF = df['isDuplicated'].duplicated()
dup = df.insert(0, 'duplicated?', duplicateRowsDF)

output = pd.ExcelWriter('output_isDuplicated.xlsx')
df.to_excel(output, 'Sheet1')
output.save()