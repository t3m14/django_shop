from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('add_to_cart/<int:product_id>/<int:user_id>/', add_to_cart, name='add_to_cart'),
    path('cart/<int:user_id>', cart, name='cart'),
]