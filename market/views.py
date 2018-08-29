from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Coin
from .forms import QuantityForm


def index(request):
    return render(request, 'market/main.html',)
    
    

def transact(request):
    
    print ( request.POST['transactionQuantity'])
    
    return HttpResponseRedirect(reverse('index'))
    