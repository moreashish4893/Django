from django.shortcuts import render,redirect
from .models import Emp

# Create your views here.

def home(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method=="POST":
        name=request.POST.get("myname")
        email=request.POST.get("myemail")
        contact=request.POST.get("mycontact")
        age=request.POST.get("myage")
        address=request.POST.get("myaddress")
        e=Emp()
        e.name=name
        e.email=email
        e.contact=contact
        e.age=age
        e.address=address
        e.save()
        return redirect('/')
    else:
        return render(request,'addemp.html') 