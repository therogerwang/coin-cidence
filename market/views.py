from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Coin
from .forms import QuantityForm


def index(request):
    return render(request, 'market/main.html',)
    
    
#request arrives, decides what to do
def transact(request):
    
    print ( request.POST['transactionQuantity'])
    
    try:
        print ( request.POST['buy'])
    except:
        print ( request.POST['sell'])
    
    print("After")
    
    
    return HttpResponseRedirect(reverse('index'))
    