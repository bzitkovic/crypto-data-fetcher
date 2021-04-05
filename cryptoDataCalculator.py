import json
import pandas as pd
from datetime import datetime, date

def CalculateAverage():   
    highestSum = 0
    lowestSum = 0
    currency = ''
    coin = ''

    fileName = input('Enter file name: ')

    with open(fileName) as data_file:    
        jsonData = json.load(data_file)
        
        for v in jsonData:
            highestSum +=  v['high']
            lowestSum += v['low']
            currency = v['currency']
            coin = v['coin']

    timeFrom = datetime.fromtimestamp(jsonData[0]['time']).strftime('%Y-%m-%d %H:%M:%S')
    timeTo = datetime.fromtimestamp(jsonData[-1]['time']).strftime('%Y-%m-%d %H:%M:%S')

    print('\nCoin: ' + coin)
    print('From: ' + timeFrom)
    print('To: ' + timeTo)
    print('Average of highest prices: ' + str(round(highestSum/len(jsonData), 4)) + ' ' + currency)
    print('Average of lowest prices: ' + str(round(lowestSum/len(jsonData), 4)) + ' ' + currency)

def CalculateVolume():
    maxVolumeFrom = 0
    maxVolumeTo = 0
    currency = ''
    coin = ''
    timeFromVolume = ''
    timeToVolume = ''

    fileName = input('Enter file name: ')

    with open(fileName) as data_file:    
        jsonData = json.load(data_file)
        
        for v in jsonData:
            currency = v['currency']
            coin = v['coin']

            if(float(v['volumefrom']) > maxVolumeFrom):
                maxVolumeFrom =  float(v['volumefrom'])
                timeFromVolume = datetime.fromtimestamp(v['time']).strftime('%Y-%m-%d %H:%M:%S')

            if(float(v['volumeto']) > maxVolumeTo):
                maxVolumeTo =  float(v['volumeto'])       
                timeToVolume = datetime.fromtimestamp(v['time']).strftime('%Y-%m-%d %H:%M:%S')

    print('\n' + coin + ' - ' + currency)
    print('Max volumene from was: ' + str(maxVolumeFrom) + ' at ' + timeFromVolume)
    print('Max volumene to was: ' + str(maxVolumeTo) + ' at ' + timeToVolume)

def main():
    while True:    
        print('\n=========================================')
        print('1. Calculate average')
        print('=========================================')
        print('2. Calculate maximun volume (from/to)')
        print('=========================================')
        print('0. Exit')
        print('=========================================')
                
        userInput = input('Choose: ')

        if(userInput == '1'):
            CalculateAverage()    
        
        if(userInput == '2'):
            CalculateVolume()
    
        if(userInput == '0'):
            break

main()