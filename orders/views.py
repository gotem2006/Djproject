from django.shortcuts import render, HttpResponseRedirect
from .forms import Orderform
# Create your views here.

def MakeOrder(request):
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = Orderform()
    return render(request, 'orders/order.html', {'form':form})
        
        