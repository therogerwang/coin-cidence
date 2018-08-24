from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Balance(models.Model):
    ''' Defines each user'''
    user_name = models.CharField(max_length = 32)
    usd_balance = models.DecimalField(max_digits=24, decimal_places=2)
    
    
class Coin(models.Model):
    '''Defines the name of the currency as well as the current held quantity. Tied to each user'''
    owner = models.ForeignKey(Balance, on_delete=models.CASCADE, null=True )
    
    coin_name = models.CharField(max_length = 60)
    quantity = models.DecimalField(default =0.0, max_digits=24, decimal_places=8) #Largest 16-digit number with 8 decimal places after