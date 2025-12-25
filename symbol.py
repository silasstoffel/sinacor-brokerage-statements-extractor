clear_symbols = {
    # Stocks
    'MOVIDA ON NM': 'MOVI3',
    'BANRISUL PNB N1': 'BRSR6',
    'MILLS': 'MILS3',
    'EVEN': 'EVEN3',
    'HYPERA': 'HYPE3',
    'ITAUUNIBANCO ON EJ N1': 'ITUB3',
    'LOG COM PROP': 'LOGG3',
    'PETRORECSA': 'RECV3',
    'VALE ON NM': 'VALE3',
    'BOA SAFRA': 'SOJA3',
    'WIZ CO': 'WIZC3',

    # FIIs
    'ITRI': 'ITRI11',
    'PORD': 'PORD11',
    'MALL11': 'MALL11',
    'RFOF11': 'RFOF11',
    'IRDM11': 'IRDM11',
    'KNRI11': 'KNRI11',
    'BARI11': 'BARI11',
    'BTHF11': 'BTHF11',
    'CLIN11': 'CLIN11',
    'VINO11': 'VINO11',
    'RVBI11': 'RVBI11',
    'LVBI11': 'LVBI11',
    'KCRE11': 'KCRE11',
    'HGBS11': 'HGBS11',
    'FIIB11': 'FIIB11',
    'IRIM11': 'IRIM11',

    # ETFs
    'ISHARES SMAL CI': 'SMLL11',
    'ISHARES BOVA CI': 'BOVA11',
}

symbol_types = {
    # fiis
    'ITRI11': 'fii',
    'PORD11': 'fii',
    'MALL11': 'fii',
    'RFOF11': 'fii',
    'IRDM11': 'fii',
    'KNRI11': 'fii',
    'BARI11': 'fii',
    'BTHF11': 'fii',
    'CLIN11': 'fii',
    'VINO11': 'fii',
    'RVBI11': 'fii',
    'LVBI11': 'fii',
    'KCRE11': 'fii',
    'HGBS11': 'fii',
    'FIIB11': 'fii', 
    'IRIM11': 'fii', 

    #stocks
    'MOVI3' : 'stock',
    'BRSR6' : 'stock',
    'MILS3' : 'stock',
    'EVEN3' : 'stock',
    'HYPE3' : 'stock',
    'ITUB3' : 'stock',
    'LOGG3' : 'stock',
    'RECV3' : 'stock',
    'VALE3' : 'stock',
    'SOJA3' : 'stock',
    'WIZC3' : 'stock',

    # etfs
    'SMLL11': 'eft',
    'BOVA11': 'eft'
}

symbols = {
    'CLEAR': clear_symbols
}

def search_symbol(text, exchange = 'CLEAR'): 
    for description, symbol in symbols[exchange].items():
        if description in text:
            return symbol
        
    return "UNKNOWN"


def search_symbol_type(symbol):
    return symbol_types.get(symbol, "")