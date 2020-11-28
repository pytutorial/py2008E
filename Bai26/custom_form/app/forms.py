# app/forms.py
from django import forms
class OrderForm(forms.Form):
    qty = forms.IntegerField(min_value=1)
    customer_name = forms.CharField()
    customer_phone = forms.CharField()
    customer_address = forms.CharField()