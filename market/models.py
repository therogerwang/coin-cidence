from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Balance(models.Model):
    """ Defines balance for each user"""
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    usd_balance = models.DecimalField(max_digits=24, decimal_places=2)
    
    def __str__(self):
        return str(self.username) + " with usd of "+ str(self.usd_balance)
    
    def update_usd_balance(self, new_balance):
        """Updates the usd balance to the inputted balance"""
        self.usd_balance = new_balance


class Coin(models.Model):
    """Defines the name of the currency as well as the current held quantity. Tied to each balance"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    
    coin_name = models.CharField(max_length = 60)
    quantity = models.DecimalField(default =0.0, max_digits=24, decimal_places=8) #Largest 16-digit number with 8 decimal places after
    
    def __str__(self):
        return str(self.owner) + " 's " + self.coin_name + " with quantity of " + str(self.quantity)
    
    def update_coin_quantity(self, new_balance):
        """Updates the coin balance to the inputted balance"""
        self.quantity = new_balance