from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('BTC/', views.btcPrice, name='btcPrice'),
    path('ETH/', views.ethPrice, name='ethPrice'),
    path('transact/', views.transact, name='transact'),
] 