from django import forms
from .models import Order

class Orderform(forms.ModelForm):
    full_name = forms.CharField(label="ФИО", widget=forms.TextInput(attrs={'class': 'form-input', "placeholder": "Фамилия Имя Отчество"}))
    phone_number = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={'class': 'form-input', "placeholder": "+ 7 999 999 99 99"}))
    email = forms.EmailField(max_length=256, label="E-mail", widget=forms.TextInput(attrs={'class': 'form-input', "placeholder": "Электронаая почта"}))
    address = forms.CharField(max_length=256, label="Адресс доставки", widget=forms.TextInput(attrs={'class': 'form-input', "placeholder": "Адресс доставки"}))
    
    
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'email', 'address')
        