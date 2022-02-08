import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from utils.gecko import *
import sqlite3
from google.oauth2 import service_account
from gsheetsdb import connect
# from historic import get_history
from datetime import datetime, time, timedelta

st.set_page_config(
   page_title="Crypto Portfolio",
     page_icon='icon.ico',
     initial_sidebar_state="expanded",
 )


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
# @st.cache
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Read df from csv, change , to . and float

df = pd.DataFrame(rows)

with st.sidebar:
    # with st.form:
    # st.
    st.write("## LOGIN:")
    user_input = st.text_input("Input password", type= 'password')
    

# Split streamlit window into 2
col1,col2 = st.columns((2,1))
page = st.columns(1)




if user_input:
    if user_input == st.secrets['tomas_private']['pass1']:
        df = df[df['Owner'] == 'Tomas']
        continue_script = True
    elif user_input == st.secrets['tomas_private']['pass2']:
        df = df[df['Owner'] == 'Dodo']
        continue_script = True
    elif user_input == st.secrets['tomas_private']['pass3']:
        df = df[df['Owner'] == 'Oco']
        continue_script = True
    else:
        col1.write("### Incorrect password")
        continue_script = False
    

    # Get info from gecko to df

    if user_input == st.secrets['tomas_private']['pass1'] or st.secrets['tomas_private']['pass2'] or st.secrets['tomas_private']['pass3']:
        if continue_script:
            coins = df['COIN'].unique().tolist()
            # coins2= [x for x in coins if x not in  ['UNI', 'XRP', 'THETA', 'BTT', 'ENJ', 'SHIB']]

            ct = datetime.now()
            start_day = datetime.combine(datetime.now(), time()) 
            week_start = start_day - timedelta(days=start_day.weekday())
            print(week_start)
            day_start_ts = start_day.timestamp()
            week_start_ts = week_start.timestamp()
            ts = ct.timestamp()


            price_dict = {}
            change_dict = {}

            try:
                for coin in coins:
                    price_dict[coin], change_dict[coin] = get_price(coin)
            except Exception as e:
                print(f'No  data for {coin} \n check if it was added to the coin list ')
            
            for index, row in df.iterrows():
                # price, change = get_price(df.at[index,'COIN'])
                price = price_dict[df.at[index,'COIN']]
                change = change_dict[df.at[index,'COIN']]
                # print(df[df['Owner'] == 'Tomas'])

                try:
                    df.at[index, 'Current_Price'] = price
                    df.at[index, 'Current_Value'] =  price * df.at[index, 'AMOUNT']
                    df.at[index, '24hChange'] = change
                    df.at[index, 'Total_Price'] = df.at[index, 'PRICE'] * df.at[index, 'AMOUNT']
                except Exception as e:
                    print (row)

            # Groupby 
            df_value = df.groupby(['COIN'])[['Current_Value', 'AMOUNT']].sum()
            df_value['Price'] = df_value['Current_Value'] / df_value['AMOUNT']
            df_price = df.groupby(['COIN'])[['Total_Price','AMOUNT']].sum()
            df_sold = df.groupby(['COIN'])[['Sold_Amount','Sold_Price', 'Sold_Value']].sum()
            df_sold = df_sold[df_sold['Sold_Amount'] > 0]
            df_change = df.groupby(['COIN'])[['24hChange']].mean()


            total_value = 0
            # Calculate current amount and profit
            for index, row in df_value.iterrows():
                try:
                    df_value.at[index,'CurrAmount'] = df_value.at[index,'AMOUNT'] - df_sold.at[index, 'Sold_Amount']
                    df_value.at[index, 'Profit'] = ((df_value.at[index, 'CurrAmount'] * df_value.at[index, 'Price']) + df_sold.at[index, 'Sold_Value']) - df_price.at[index, 'Total_Price']
                except KeyError:
                    df_value.at[index, 'CurrAmount'] = df_value.at[index, 'AMOUNT']
                    df_value.at[index, 'Profit'] = (df_value.at[index, 'CurrAmount'] * df_value.at[index, 'Price']) - df_price.at[index, 'Total_Price']


            print(df_value)
            # Calculate total profit
            total_profit = df_value['Profit'].sum()
            total_spent = df_price['Total_Price'].sum()
            total_sold = df_sold['Sold_Value'].sum()
            net_spent = df_price['Total_Price'].sum() - df_sold['Sold_Value'].sum()
            total_value = (df_value['Price']*df_value['CurrAmount']).sum()
            
            print(df_price)

            # Sort df's
            final_df = df_value.drop(['AMOUNT','Current_Value'] ,axis=1)
            final_df = final_df.sort_values(by=['Profit'], ascending = False)

            df_change['positive_change'] = df_change['24hChange'] > 0
            df_change = df_change.sort_values(by = ['24hChange'] , ascending = True)



            # Show main stats
            col1.write("# Crypto portfolio \n ### by TrimPeachu")
            col1.write("#### TOTAL PROFIT: {:.2f} €".format(total_profit))
            col1.write("#### NET SPENT: {:.2f} €".format(net_spent))
            col1.write("##### TOTAL VALUE: {:.2f} €".format(total_value))
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

            # history_option = st.selectbox("Would you like to see your portfolio profit history chart?" ('Yes', 'No'))
            with st.sidebar:
                
                if st.button("Show history chart"):
                    history_df = pd.DataFrame()


                    for coin in coins:
                        if len(history_df) > 0:
                            history_df[coin] = get_history(coin, ts, history_df)[coin]
                        else:
                            history_df = history_df.append(get_history(coin, ts, history_df))
                    
                    history_df['Date'] = pd.to_datetime(history_df['Date'], unit = 'ms').dt.normalize()

                    currencies = history_df.columns.tolist()
                    currencies[:] = [x for x in currencies if x != 'Date']


                    history_df['Value'] = 0

                    for coin in currencies:
                        for index, row in history_df.iterrows():
                            history_df.at[index, 'Value'] = history_df.at[index, 'Value'] + (history_df.at[index, coin]*final_df.at[coin,'CurrAmount'])


                    price = df_price.sum(axis=0)
                    price = price['Total_Price']
                    sold = df_sold.sum(axis=0)
                    sold = sold['Sold_Value']

                    history_df['Profit'] = history_df['Value'] + sold - price
                    history_df = history_df.set_index('Date')
                    history_profit = history_df['Profit'] 

                    print(history_df)
                    print(history_profit)

                    col1.line_chart(history_profit)
                    col1.dataframe(history_df)
                
                if st.button("Show today's movement"):
                    today_df = pd.DataFrame()
                    print(ts)
                    print(day_start_ts)

                    for coin in coins:
                        if len(today_df) > 0:
                            today_df[coin] = get_today_chart(coin,day_start_ts,ts,today_df)[coin]
                        else:
                            today_df = today_df.append(get_today_chart(coin,day_start_ts,ts,today_df))
                    
                    
                    today_df['Date'] = pd.to_datetime(today_df['Date'], unit = 'ms')

                    currencies = today_df.columns.tolist()
                    currencies[:] = [x for x in currencies if x != 'Date']


                    today_df['Value'] = 0

                    for coin in currencies:
                        for index, row in today_df.iterrows():
                            today_df.at[index, 'Value'] = today_df.at[index, 'Value'] + (today_df.at[index, coin]*final_df.at[coin,'CurrAmount'])


                    price = df_price.sum(axis=0)
                    price = price['Total_Price']
                    sold = df_sold.sum(axis=0)
                    sold = sold['Sold_Value']

                    today_df['Profit'] = today_df['Value'] + sold - price
                    today_df = today_df.set_index('Date')
                    today_profit = today_df['Profit'] 

                    print(today_df)
                    print(today_profit)

                    col1.line_chart(today_profit)
                    col1.dataframe(today_df)

                            
                if st.button("Show this week's movement"):
                    week_df = pd.DataFrame()
                    print(ts)
                    print(week_start_ts)

                    for coin in coins:
                        if len(week_df) > 0:
                            week_df[coin] = get_today_chart(coin,week_start_ts,ts,week_df)[coin]
                        else:
                            week_df = week_df.append(get_today_chart(coin,week_start_ts,ts,week_df))
                    
                    
                    week_df['Date'] = pd.to_datetime(week_df['Date'], unit = 'ms')

                    currencies = week_df.columns.tolist()
                    currencies[:] = [x for x in currencies if x != 'Date']


                    week_df['Value'] = 0

                    for coin in currencies:
                        for index, row in week_df.iterrows():
                            week_df.at[index, 'Value'] = week_df.at[index, 'Value'] + (week_df.at[index, coin]*final_df.at[coin,'CurrAmount'])


                    price = df_price.sum(axis=0)
                    price = price['Total_Price']
                    sold = df_sold.sum(axis=0)
                    sold = sold['Sold_Value']

                    week_df['Profit'] = week_df['Value'] + sold - price
                    week_df = week_df.set_index('Date')
                    week_profit = week_df['Profit'] 

                    print(week_df)
                    print(week_profit)

                    col1.line_chart(week_profit)
                    col1.dataframe(week_df)
            
                if st.button("Best picks"):
                    df_pick = pd.DataFrame()
                    print(df)
                    df_pick['coin'] = df['COIN']
                    df_pick['bought_Price'] = df['PRICE']
                    df_pick['amount'] = df['AMOUNT']
                    df_pick['curr_Price'] = df['Current_Price']
                    df_pick['x'] = df_pick['curr_Price'] / df_pick['bought_Price']

                    df_pick = df_pick.sort_values(by=['coin', 'bought_Price'])
                    df_pick = df_pick.drop_duplicates(subset = ['coin'])
                    df_pick = df_pick.sort_values(by=['x'], ascending = False)
                    df_pick = df_pick.set_index('coin')

                    col1.table(df_pick)
                
                # if st.button('Best sold'):
                #     df_best_sold = df_sold
                #     for index, row in df_best_sold.iterrows():
                #         df_best_sold.at[index,'curr_Price'] = final_df[index,'Price']
                #     # df_best_sold['x'] = df_best_sold
                #     # df_best_sold = df_best_sold.sort_values(by=['x'])
                #     col1.table(df_best_sold)


                    
                    
            
            # if st.button('Show my diversity'):
            #    plt.figure(figsize=(16,8))
            #    ax1 = plt.subplot(121,aspect='equal')
            #    df_price.plot(kind='pie', y= df_price['Total_Price'], ax = ax1, labels = df_price['COIN'])
            #    st.write(plt.show())

            

        else:
            col1.write('Try again')

