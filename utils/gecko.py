from typing_extensions import final
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import pandas as pd 
cg = CoinGeckoAPI()

def get_price(currency):
    # print(currency)
    if currency == 'ADA':
        price = cg.get_price(ids ='cardano', vs_currencies = 'eur' , include_24hr_change='true')
        curr = 'cardano'
    elif currency == 'LTC':
        price = cg.get_price(ids ='litecoin', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'litecoin'
    elif currency == 'LINK':
        price = cg.get_price(ids ='chainlink', vs_currencies = 'eur', include_24hr_change = 'true')
        curr = 'chainlink'
    elif currency == 'UNI':
        price = cg.get_price(ids ='uniswap', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'uniswap'
    elif currency == 'XRP':
        price = cg.get_price(ids ='ripple', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'ripple'
    elif currency == 'ETH':
        price = cg.get_price(ids ='ethereum', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'ethereum'
    elif currency == 'XLM':
        price = cg.get_price(ids ='stellar', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'stellar'
    elif currency == 'THETA':
        price = cg.get_price(ids ='theta-token', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'theta-token'
    elif currency == 'DOGE':
        price = cg.get_price(ids ='dogecoin', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'dogecoin'
    elif currency == 'MATIC':
        price = cg.get_price(ids = 'matic-network', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'matic-network'
    elif currency == 'EOS':
        price = cg.get_price(ids = 'eos', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'eos'
    elif currency == 'DOT':
        price = cg.get_price(ids = 'polkadot', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'polkadot'
    elif currency == 'BTT':
        price = cg.get_price(ids = 'bittorrent-2', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'bittorrent-2'
    elif currency == 'ENJ':
        price = cg.get_price(ids = 'enjincoin', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'enjincoin'
    elif currency == 'SHIB':
        price = cg.get_price(ids = 'shiba-inu', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'shiba-inu'
    elif currency == 'BTC':
        price = cg.get_price(ids = 'bitcoin', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'bitcoin'
    elif currency == 'CRO':
        price = cg.get_price(ids = 'crypto-com-chain', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'crypto-com-chain'
    elif currency == 'ALGO':
        price = cg.get_price(ids = 'algorand', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'algorand'
    elif currency == 'TFUEL':
        price = cg.get_price(ids = 'theta-fuel', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'theta-fuel'
    elif currency == 'SOL':
        price = cg.get_price(ids = 'solana', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'solana'
    elif currency == 'REN':
        price = cg.get_price(ids = 'republic-protocol', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'republic-protocol'
    elif currency == 'FLOW':
        price = cg.get_price(ids = 'flow', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'flow'
    elif currency == 'AVAX':
        price = cg.get_price(ids = 'avalanche-2', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'avalanche-2'
    elif currency == '1INCH':
        price = cg.get_price(ids = '1inch', vs_currencies = 'eur', include_24hr_change='true')
        curr = '1inch'
    elif currency == 'NMP':
        price = cg.get_price(ids = 'neuromorphic-io', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'neuromorphic-io'
    elif currency == 'VET':
        price = cg.get_price(ids = 'vechain', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'vechain'
    elif currency == 'EGLD':
        price = cg.get_price(ids = 'elrond-erd-2', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'elrond-erd-2'
    elif currency == 'ATOM':
        price = cg.get_price(ids = 'cosmos', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'cosmos'
    elif currency == 'ONE':
        price = cg.get_price(ids = 'harmony', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'harmony'
    elif currency == 'NMR':
        price = cg.get_price(ids = 'numeraire', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'numeraire'
    elif currency == 'STMX':
        price = cg.get_price(ids = 'storm', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'storm'
    elif currency == 'CAKE':
        price = cg.get_price(ids = 'pancakeswap-token', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'pancakeswap-token'
    elif currency == 'BNB':
        price = cg.get_price(ids = 'binancecoin', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'binancecoin'
    elif currency == 'CHZ':
        price = cg.get_price(ids = 'chiliz', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'chiliz'
    elif currency == 'CTSI':
        price = cg.get_price(ids = 'cartesi', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'cartesi'
    elif currency == 'LUNA':
        price = cg.get_price(ids = 'terra-luna', vs_currencies = 'eur', include_24hr_change='true')
        curr = 'terra-luna'

    


    clean_price = price.get(curr, {}).get('eur')
    clean_24 = price.get(curr, {}).get('eur_24h_change')
    return(clean_price, clean_24)   

def get_history(currency, timestamp, df):
    if currency == 'ADA':
        history_price = cg.get_coin_market_chart_range_by_id(id ='cardano', vs_currency = 'eur' , from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'cardano'
    elif currency == 'LTC':
        history_price = cg.get_coin_market_chart_range_by_id(id ='litecoin', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'litecoin'
    elif currency == 'LINK':
        history_price = cg.get_coin_market_chart_range_by_id(id ='chainlink', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'chainlink'
    elif currency == 'UNI':
        history_price = cg.get_coin_market_chart_range_by_id(id ='uniswap', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'uniswap'
    elif currency == 'XRP':
        history_price = cg.get_coin_market_chart_range_by_id(id ='ripple', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'ripple'
    elif currency == 'ETH':
        history_price = cg.get_coin_market_chart_range_by_id(id ='ethereum', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'ethereum'
    elif currency == 'XLM':
        history_price = cg.get_coin_market_chart_range_by_id(id ='stellar', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'stellar'
    elif currency == 'THETA':
        history_price = cg.get_coin_market_chart_range_by_id(id ='theta-token', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'theta-token'
    elif currency == 'DOGE':
        history_price = cg.get_coin_market_chart_range_by_id(id ='dogecoin', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'dogecoin'
    elif currency == 'MATIC':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'matic-network', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'matic-network'
    elif currency == 'EOS':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'eos', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'eos'
    elif currency == 'DOT':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'polkadot', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'polkadot'
    elif currency == 'BTT':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'bittorrent-2', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'bittorrent-2'
    elif currency == 'ENJ':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'enjincoin', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'enjincoin'
    elif currency == 'SHIB':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'shiba-inu', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'shiba-inu'
    elif currency == 'BTC':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'bitcoin', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'bitcoin'
    elif currency == 'CRO':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'crypto-com-chain', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'crypto-com-chain'
    elif currency == 'ALGO':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'algorand', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'algorand'
    elif currency == 'TFUEL':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'theta-fuel', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'theta-fuel'
    elif currency == 'SOL':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'solana', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'solana'
    elif currency == 'REN':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'republic-protocol', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'republic-protocol'
    elif currency == 'FLOW':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'flow', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'flow'
    elif currency == 'AVAX':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'avalanche-2', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'avalanche-2'
    elif currency == '1INCH':
        history_price = cg.get_coin_market_chart_range_by_id(id = '1inch', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = '1inch'
    elif currency == 'NMP':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'neuromorphic-io', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'neuromorphic-io'
    elif currency == 'VET':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'vechain', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'vechain'
    elif currency == 'EGLD':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'elrond-erd-2', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'elrond-erd-2'
    elif currency == 'ATOM':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'cosmos', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'cosmos'
    elif currency == 'ONE':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'harmony', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'harmony'
    elif currency == 'NMR':
        history_price = cg.get_coin_market_chart_range_by_id(id = 'numeraire', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'numeraire'
    elif currency == 'STMX':
        history_price = cg.get_coin_market_chart_range_by_id(ids = 'storm', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'storm'
    elif currency == 'CAKE':
        history_price = cg.get_coin_market_chart_range_by_id(ids = 'pancakeswap-token', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'pancakeswap-token'
    elif currency == 'BNB':
        history_price = cg.get_coin_market_chart_range_by_id(ids = 'binancecoin', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'binancecoin'
    elif currency == 'CHZ':
        history_price = cg.get_coin_market_chart_range_by_id(ids = 'chiliz', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'chiliz'
    elif currency == 'CTSI':
        history_price = cg.get_coin_market_chart_range_by_id(ids = 'cartesi', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'cartesi'
    elif currency == 'LUNA':
        history_price = cg.get_coin_market_chart_range_by_id(ids = 'terra-luna', vs_currency = 'eur', from_timestamp = '1619900343', to_timestamp = str(timestamp))
        curr = 'terra-luna'
    
    history_price = history_price['prices']

    if len(df) > 0:
        just_history_price = [el[1] for el in history_price]
        try:
            df[currency] = just_history_price
        except:
            print(currency, just_history_price, history_price)
        
    else:
        df = pd.DataFrame(history_price, columns = ['Date', currency])

    return df


def get_today_chart(currency, start_day, timestamp, df):
    if currency == 'ADA':
        today_price = cg.get_coin_market_chart_range_by_id(id ='cardano', vs_currency = 'eur' , from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'cardano'
    elif currency == 'LTC':
        today_price = cg.get_coin_market_chart_range_by_id(id ='litecoin', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'litecoin'
    elif currency == 'LINK':
        today_price = cg.get_coin_market_chart_range_by_id(id ='chainlink', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'chainlink'
    elif currency == 'UNI':
        today_price = cg.get_coin_market_chart_range_by_id(id ='uniswap', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'uniswap'
    elif currency == 'XRP':
        today_price = cg.get_coin_market_chart_range_by_id(id ='ripple', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'ripple'
    elif currency == 'ETH':
        today_price = cg.get_coin_market_chart_range_by_id(id ='ethereum', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'ethereum'
    elif currency == 'XLM':
        today_price = cg.get_coin_market_chart_range_by_id(id ='stellar', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'stellar'
    elif currency == 'THETA':
        today_price = cg.get_coin_market_chart_range_by_id(id ='theta-token', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'theta-token'
    elif currency == 'DOGE':
        today_price = cg.get_coin_market_chart_range_by_id(id ='dogecoin', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'dogecoin'
    elif currency == 'MATIC':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'matic-network', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'matic-network'
    elif currency == 'EOS':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'eos', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'eos'
    elif currency == 'DOT':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'polkadot', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'polkadot'
    elif currency == 'BTT':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'bittorrent-2', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'bittorrent-2'
    elif currency == 'ENJ':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'enjincoin', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'enjincoin'
    elif currency == 'SHIB':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'shiba-inu', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'shiba-inu'
    elif currency == 'BTC':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'bitcoin', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'bitcoin'
    elif currency == 'CRO':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'crypto-com-chain', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'crypto-com-chain'
    elif currency == 'ALGO':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'algorand', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'algorand'
    elif currency == 'TFUEL':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'theta-fuel', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'theta-fuel'
    elif currency == 'SOL':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'solana', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'solana'
    elif currency == 'REN':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'republic-protocol', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'republic-protocol'
    elif currency == 'FLOW':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'flow', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'flow'
    elif currency == 'AVAX':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'avalanche-2', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'avalanche-2'
    elif currency == '1INCH':
        today_price = cg.get_coin_market_chart_range_by_id(id = '1inch', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = '1inch'
    elif currency == 'NMP':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'neuromorphic-io', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'neuromorphic-io'
    elif currency == 'VET':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'vechain', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'vechain'
    elif currency == 'EGLD':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'elrond-erd-2', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'elrond-erd-2'
    elif currency == 'ATOM':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'cosmos', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'cosmos'
    elif currency == 'ONE':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'harmony', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'harmony'
    elif currency == 'NMR':
        today_price = cg.get_coin_market_chart_range_by_id(id = 'numeraire', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'numeraire'
    elif currency == 'STMX':
        price = cg.get_coin_market_chart_range_by_id(ids = 'storm', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'storm'
    elif currency == 'CAKE':
        price = cg.get_coin_market_chart_range_by_id(ids = 'pancakeswap-token', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'pancakeswap-token'
    elif currency == 'BNB':
        price = cg.get_coin_market_chart_range_by_id(ids = 'binancecoin', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'binancecoin'
    elif currency == 'CHZ':
        price = cg.get_coin_market_chart_range_by_id(ids = 'chiliz', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'chiliz'
    elif currency == 'CTSI':
        price = cg.get_coin_market_chart_range_by_id(ids = 'cartesi', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'cartesi'
    elif currency == 'LUNA':
        price = cg.get_coin_market_chart_range_by_id(ids = 'terra-luna', vs_currency = 'eur', from_timestamp = start_day, to_timestamp = str(timestamp))
        curr = 'terra-luna'
    

    today_price = today_price['prices']

    if len(df) > 0:
        rows = df.shape[0]
        just_today_price = [el[1] for el in today_price]
        difference = len(just_today_price) - rows 

        
        if difference != 0:
            if difference < 0: 
                difference = (difference * (-1))
                print(difference)
                for i in range(difference):
                    just_today_price.append(just_today_price[-1])
            elif difference > 0:
                for i in range(difference):
                    del just_today_price[-1]


        # try:
        df[currency] = just_today_price
        print(df)
        # except:
            # print(currency, just_today_price, today_price)
        
    else:
        df = pd.DataFrame(today_price, columns = ['Date', currency])

    return df
