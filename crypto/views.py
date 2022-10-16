from django.shortcuts import render
import requests
import json


def home(request):
    '''
    Grab Crypto Price Data
    '''
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOT,TRX&tsyms=INR")
    price = json.loads(price_request.content)
    
    '''
    Grab Crypto News
    '''
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api':api, 'price':price})

def prices(request):
    if request.method=='POST': 
        quote=request.POST['quote']
        crypto_request = requests.get(f"https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote.upper()}&tsyms=INR")
        crypto = json.loads(crypto_request.content)

        return render(request,'prices.html',{'quote':quote, 'crypto':crypto})
    else:
        notFound = 'Enter the crypto code in the above search box to get details!'
        return render(request,'prices.html',{'notFound':notFound})    