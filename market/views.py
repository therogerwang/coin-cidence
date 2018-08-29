from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Coin
from .forms import QuantityForm

def index(request):
    return render(request, 'market/main.html',)
    
    


    