from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Balance, Coin
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
    transact_price = Decimal(request.POST['transact_price'])
    user_id = request.POST['user_id']
    
    print("USER =", user_id )
    print (transactQuantity, coin_type, transact_price)
    
    ##TEMP SOLUTION BELOW
    try:
        #BUY
        print ( request.POST['buy'])
        cost = transactQuantity * transact_price
        user_balance = get_object_or_404(Balance,id=user_id)
        print ("Balance gotten = ", user_balance)
        print("New balance",user_balance.usd_balance - cost)
        user_balance.update_usd_balance(user_balance.usd_balance - cost)
        user_balance.save()

        
    except:
        #SELL
        print ( request.POST['sell'])
        
        
    
    print("After")
    
    
    return HttpResponseRedirect(reverse('index'))
    