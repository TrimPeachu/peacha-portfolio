from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def get_price(currency):
    print(currency)
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


    clean_price = price.get(curr, {}).get('eur')
    clean_24 = price.get(curr, {}).get('eur_24h_change')
    return(clean_price, clean_24)   