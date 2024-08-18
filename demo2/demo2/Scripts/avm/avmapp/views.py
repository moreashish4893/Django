from django.shortcuts import render,redirect
from .models import Emp,Empform

# Create your views here.

def home(request):
    return render(request,'home.html')


def add_emp(request):
    if request.method=='POST':
        f=Empform(request.POST)
        f.save()
        return redirect('/')
    else:
        f=Empform
        context={'form':f}
        return render(request,'addemp.html',context)
