from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Coin
from .forms import QuantityForm
from decimal import *



#SETTING DECIMAL BASED MATH
getcontext().prec = 8


def index(request):
    return render(request, 'market/main.html',)
    

def transact(request):
    """ Decides what happens with the Transact (buy/sell) POST request when it 
    is received """
    

    transactQuantity = Decimal(request.POST['transactionQuantity'])
    coin_type = request.POST['coin_type']
    transact_price = request.POST['transact_price']
    print (transactQuantity, coin_type, transact_price)
    
    
    ##TEMP SOLUTION BELOW
    try:
        #BUY
        print ( request.POST['buy'])

        
    except:
        #SELL
        print ( request.POST['sell'])
    
    print("After")
    
    
    return HttpResponseRedirect(reverse('index'))
    