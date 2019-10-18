from django.urls import path, include
from .views import billing, payment, charge
from .models import Billing_Address, Delivery_Address
from .forms import Billing_Address_Form, Delivery_Address_Form

app_name = 'payment'
urlpatterns = [
    path('bill<id>', billing, name="billing"),
    path('pay<id>', payment, name="payment"),
    path('success<id>', charge, name="paid")
]