def cripto():
    print('Информация по курсам криптовалют')
    answer = input('(1) Доллар США - Bitcoin, (2) Доллар США - Ethereum')
    if answer == '1':
        data_USD_BTC=requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=USD-BTC')
        print(data_USD_BTC.json())
    if answer == '2':
        data_USD_ETH=requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=USD-BTC')
        print(data_USD_ETH.json())
