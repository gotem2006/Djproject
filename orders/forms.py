from django import forms
from .models import Order

class Orderform(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(max_length=256)
    adress = forms.CharField(max_length=256)
    
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'adress')
        