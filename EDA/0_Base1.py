import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the display options
pd.options.display.float_format = '{:,.0f}'.format
pd.set_option('display.max_rows', 1000)


#laod data 
df = pd.read_parquet('../data/transactions.parquet')


#basic info on the data
# getting nb of missing values in each column
#getting the duplicates in the data

print(f'number of columns : {len(df.columns)} ')
print (f'number of rows : {len(df)} ')
print(f'number of duplicated rows : {df.duplicated().sum()} ')  
print('\n')
print('Number of NULL value :')
print(df.isna().sum())
print('\n')




