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

    # ETFs
    'ISHARES SMAL CI': 'SMLL11',
    'ISHARES BOVA CI': 'BOVA11',
}

symbols = {
    'CLEAR': clear_symbols
}

def search_symbol(text, exchange = 'CLEAR'): 
    for description, symbol in symbols[exchange].items():
        if description in text:
            return symbol
        
    return "UNKNOWN"