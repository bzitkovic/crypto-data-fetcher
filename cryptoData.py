import cryptocompare as cc
from datetime import datetime, date
import json
import pandas as pd

# You can get your API_KEY at: https://min-api.cryptocompare.com/
cc.cryptocompare._set_api_key_parameter('')

def GetCurrentPrice():
    coin = input('Enter desired coin (BTC, ETH, ...): ')
    currency = input('Enter desired currency (USD, EUR, ...): ')
    save = input('Save data to file? y/n ')

    result = cc.get_price(coin, currency=currency)
    print(result)

    if(save == 'y'):
        now = datetime.now()
        current_time = now.strftime('%Y-%m-%d %H:%M:%S')

        result['currency'] = currency
        result['time'] = current_time 

        string = json.dumps(result)
        df = pd.read_json(string)
        df.to_csv('Prices.csv', mode='a', encoding='utf-8', index=False)

def ListAllCoins():
     coins = cc.get_coin_list(format=True)        
     for coin in coins:        
         print(coin + '\n')

def GetDataForDay():
    coin = input('\nEnter desired coin (BTC, ETH, ...): ')
    currency = input('Enter desired currency (USD, EUR, ...): ')
    save = input('Save data to file? y/n ')

    result = cc.get_historical_price_day(coin, currency=currency, limit=30)

    for value in result:
        ts = datetime.fromtimestamp(value['time']).strftime('%Y-%m-%d')
        print('===============================================')
        print('Time: ' + str(ts) + ', High: ' + str(value['high']) + ', Low: ' + str(value['low']))

    print('===============================================')

    if(save == 'y'):
        for day in result:   
            day['coin'] = coin
            day['currency'] = currency            

        #Save as json
        with open('Crypto_Data_For_Day_' + ts + '.json', 'w') as fp:
            json.dump(result, fp)

        #Save as csv
        string = json.dumps(result)
        df = pd.read_json(string)
        df.to_csv('Crypto_Data_For_Day_' + ts + '.csv', mode='w', encoding='utf-8', index=False)

def GetDataForHour():
    coin = input('\nEnter desired coin (BTC, ETH, ...): ')
    currency = input('Enter desired currency (USD, EUR, ...): ')
    save = input('Save data to file? y/n ')

    now = datetime.now()
    current_time = now.strftime('%Y-%m-%d')

    result = cc.get_historical_price_hour(coin, currency=currency, limit=24)

    for value in result:
        ts = datetime.fromtimestamp(value['time']).strftime('%Y-%m-%d %H:%M:%S')
        print('===============================================')
        print('Time: ' + str(ts) + ', High: ' + str(value['high']) + ', Low: ' + str(value['low']))

    print('===============================================')

    if(save == 'y'):
        for hour in result:
            hour['coin'] = coin
            hour['currency'] = currency
 
        with open('Crypto_Data_For_Hour_' + current_time + '.json', 'w') as fp:
            json.dump(result, fp)

        string = json.dumps(result)
        df = pd.read_json(string)
        df.to_csv('Crypto_Data_For_Hour_' + current_time + '.csv', mode='w', encoding='utf-8', index=False)

def GetDataForMinute():
    coin = input('\nEnter desired coin (BTC, ETH, ...): ')
    currency = input('Enter desired currency (USD, EUR, ...): ')
    save = input('Save data to file? y/n ')

    now = datetime.now()
    current_time = now.strftime('%Y-%m-%d')

    result = cc.get_historical_price_minute(coin, currency=currency, limit=300)

    for coin in result:
        ts = datetime.fromtimestamp(coin['time']).strftime('%Y-%m-%d %H:%M:%S')
        print('===============================================')
        print('Time: ' + str(ts) + ', High: ' + str(coin['high']) + ', Low: ' + str(coin['low']))

    print('===============================================')

    if(save == 'y'):
        for minute in result:        
            minute['currency'] = currency

    with open('Crypto_Data_For_Minute_' + current_time + '.json', 'w') as fp:
        json.dump(result, fp)

    string = json.dumps(result)
    df = pd.read_json(string)
    df.to_csv('Crypto_Data_For_Minute_' + current_time + '.csv', mode='w', encoding='utf-8', index=False)

def GetExchanges():
    excahnges = cc.get_exchanges()

    for exchange in excahnges:
        print('===============================================')
        print('Name: ' + str(exchange))
        print('===============================================')

def main():
    while True:    
        print('\n=========================================')
        print('1. Get current price')
        print('=========================================')
        print('2. List all coins')
        print('=========================================')
        print('3. Get historical data for day')
        print('=========================================')
        print('4. Get historical data for hour')
        print('=========================================')
        print('5. Get historical data for minute')
        print('=========================================')
        print('6. Get excanges')
        print('=========================================')
        print('0. Exit')
        print('=========================================')
                
        userInput = input('Choose: ')

        if(userInput == '1'):
            GetCurrentPrice()
    
        if(userInput == '2'):
            ListAllCoins()

        if(userInput == '3'):
            GetDataForDay()

        if(userInput == '4'):
            GetDataForHour()

        if(userInput == '5'):
            GetDataForMinute()

        if(userInput == '6'):
            GetExchanges()
        
        if(userInput == '0'):
            break

main()