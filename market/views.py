from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Balance, Coin
from .forms import QuantityForm
from decimal import *



#SETTING DECIMAL BASED MATH
getcontext().prec = 8


def index(request):
    # return render(request, 'market/main.html')
    return HttpResponseRedirect(reverse('btcPrice'))
    
def btcPrice(request):
    return render(request, 'market/main.html')
    
    
def ethPrice(request):
    return render(request, 'market/ethPrice.html')
    
# def nanoPage(request):
#     return render(request, 'market/main.html')



def transact(request):
    """ Decides what happens with the Transact (buy/sell) POST request when it 
    is received """
    
    transactQuantity = Decimal(request.POST['transactionQuantity'])
    coin_type = request.POST['coin_type']
    transact_price = Decimal(request.POST['transact_price'])
    user_id = request.POST['user_id']
    submit_type = request.POST['submit_type']
    
    print("USER =", user_id )
    print (transactQuantity, coin_type, transact_price)
    
    
    if submit_type == 'buy':
        #BUY
        print ("BUYING")
        
        # subtract cost from usd balance
        cost = transactQuantity * transact_price
        user_balance = get_object_or_404(Balance,id=user_id)
        user_balance.update_usd_balance(user_balance.usd_balance - cost)
        user_balance.save()
        
        # add new coin quantity
        username = user_balance.username
        # coin_balance = Coin.objects.filter(owner__username__exact = user_id)
        coin_balance = get_object_or_404(Coin, owner__username__exact = username)
        coin_balance.update_coin_quantity( coin_balance.quantity + transactQuantity )
        print(coin_balance)
        coin_balance.save()
    
    elif submit_type == 'sell':
        #SELL
        print("SELLING")
        
        #Add revenue to usd balance
        revenue = transactQuantity * transact_price
        user_balance = get_object_or_404(Balance,id=user_id)
        user_balance.update_usd_balance(user_balance.usd_balance + revenue)
        user_balance.save()
        
        #Subtract from coin quantity
        username = user_balance.username
        coin_balance = get_object_or_404(Coin, owner__username__exact = username)
        coin_balance.update_coin_quantity( coin_balance.quantity - transactQuantity )
        coin_balance.save()
        
    else:
        print("RAISE EXCEPTION HERE")
    
        
        
    
    print("After")
    
    return HttpResponseRedirect(reverse('index'))
    