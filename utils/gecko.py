from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def get_price(currency):
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
    clean_price = price.get(curr, {}).get('eur')
    clean_24 = price.get(curr, {}).get('eur_24h_change')
    return(clean_price, clean_24)