from django import forms

class QuantityForm(forms.Form):
    transact_quantity = forms.IntegerField()