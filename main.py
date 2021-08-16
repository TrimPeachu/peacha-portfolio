import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from utils.gecko import *
import sqlite3
from google.oauth2 import service_account
from gsheetsdb import connect

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Read df from csv, change , to . and float

df = pd.DataFrame(rows)
print(df)

# df = pd.read_csv('data\portfolio.csv', delimiter= ';')
# df = df.apply(lambda x: x.str.replace(',','.'))
# df = df.apply(pd.to_numeric, errors='ignore')

# Get info from gecko to df
for index, row in df.iterrows():
    price, change = get_price(df.at[index,'COIN'])
    df.at[index, 'Current_Price'] = price
    df.at[index, 'Current_Value'] =  price * df.at[index, 'AMOUNT']
    df.at[index, '24hChange'] = change
    df.at[index, 'Total_Price'] = df.at[index, 'PRICE'] * df.at[index, 'AMOUNT']

# Groupby 
df_value = df.groupby(['COIN'])[['Current_Value', 'AMOUNT']].sum()
df_value['Price'] = df_value['Current_Value'] / df_value['AMOUNT']
df_price = df.groupby(['COIN'])[['Total_Price','AMOUNT']].sum()
df_sold = df.groupby(['COIN'])[['Sold_Amount','Sold_Price', 'Sold_Value']].sum()
df_sold = df_sold[df_sold['Sold_Amount'] > 0]
df_change = df.groupby(['COIN'])[['24hChange']].mean()


# Calculate current amount and profit
for index, row in df_value.iterrows():
    try:
        df_value.at[index,'CurrAmount'] = df_value.at[index,'AMOUNT'] - df_sold.at[index, 'Sold_Amount']
        df_value.at[index, 'Profit'] = ((df_value.at[index, 'CurrAmount'] * df_value.at[index, 'Price']) + df_sold.at[index, 'Sold_Value']) - df_price.at[index, 'Total_Price']

    except KeyError:
        df_value.at[index, 'CurrAmount'] = df_value.at[index, 'AMOUNT']
        df_value.at[index, 'Profit'] = (df_value.at[index, 'CurrAmount'] * df_value.at[index, 'Price']) - df_price.at[index, 'Total_Price']

# Calculate total profit
total_profit = df_value['Profit'].sum()
total_spent = df_price['Total_Price'].sum()
total_sold = df_sold['Sold_Value'].sum()
net_spent = df_price['Total_Price'].sum() - df_sold['Sold_Value'].sum()

# Sort df's
final_df = df_value.drop(['AMOUNT','Current_Value'] ,axis=1)
final_df = final_df.sort_values(by=['Profit'], ascending = False)

df_change['positive_change'] = df_change['24hChange'] > 0
df_change = df_change.sort_values(by = ['24hChange'] , ascending = True)


# Split streamlit window into 2
col1,col2 = st.columns((2,1))

# Show main stats
col1.write("# Crypto portfolio \n ### by TrimPeachu")
col1.write("#### TOTAL PROFIT: {:.2f} €".format(total_profit))
col1.write("#### NET SPENT: {:.2f} €".format(net_spent))
col1.write("##### TOTAL SPENT: {:.2f} €".format(total_spent))
col1.write("##### TOTAL SOLD: {:.2f} €".format(total_sold))

# Create tables and charts
col1.bar_chart(final_df['Profit'] )
col1.table(final_df)
plt.figure(figsize=(5,25))
plt.subplots_adjust(top = 1, bottom = 0)
df_change['24hChange'].plot(kind='barh', color=df_change.positive_change.map({True: 'g', False: 'r'}))
col2.write("### 24h Change%")
col2.pyplot(plt)


