
# toolkit for data analysis
import pandas as pd

# toolkit for system management
import os

# import .dbf file
from dbfread import DBF

# toolkit for data analysis
import numpy as np

# toolkit for system management
import sys

# import .dbf file
from dbfread import DBF

# set working directory
os.chdir('D:/')

# read 'ENOEN_SDEMT221.dbf' file and store it in a dataframe
df = pd.DataFrame(list(DBF('ENOEN_SDEMT221.dbf')))

# get column names and print them
print(df.columns)

# convert EDA, R_DEF and C_RES to numeric
df['EDA'] = pd.to_numeric(df['EDA'])
df['R_DEF'] = pd.to_numeric(df['R_DEF'])
df['C_RES'] = pd.to_numeric(df['C_RES'])

# filter data where EDA is between 15 and 97 and R_DEF is 0 and C_RES is 1 or 3
df_1 = df[(df['EDA'] >= 15) & (df['EDA'] <= 97) & (df['R_DEF'] == 0) & ((df['C_RES'] == 1) | (df['C_RES'] == 3))]

# sum 'FAC_TRI' aggregated by 'CLASE2'
df_2 = df_1.groupby('CLASE2').sum()['FAC_TRI']

# print df_2
print(df_2)


