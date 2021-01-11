import numpy as np
import pandas as pd

df = pd.read_csv('example')

df.to_csv('My_output', index=False)
print(pd.read_csv('My_output'))

df1 = pd.read_excel('Excel_Sample_diff_format.xls', sheet_name='Sheet1')
print('temp',df1)

df1.to_excel('excel_sample2_temp.xlsx', sheet_name='NewSheet')
print('done')