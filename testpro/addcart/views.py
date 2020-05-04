from django.shortcuts import render
from addcart.forms import items
# Create your views here.
def add(request):
    forms=items()
    if request.method=="POST":
        name=request.POST["name"]
        quantity=request.POST["quantity"]
        request.session[name]=quantity
        #request.session.set_expiry(100)
    return render(request,"addcart/add.html",{"form":forms})
def display(request):
    return render(request,"addcart/display.html")