from django.shortcuts import render,redirect
from.models import Income,IncomeForm

# Create your views here.
from django.contrib.auth.models import User

def add_income(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        #f=IncomeForm(request.POST)
        income=request.POST.get('income')     
        income_type=request.POST.get('income_type')     
        income_date=request.POST.get('income_date')     
        description=request.POST.get('description')     
        inc=Income()
        inc.income=income
        inc.income_type=income_type
        inc.income_date=income_date
        inc.description=description
        inc.user=User.objects.get(id=uid)
        inc.save()
        return redirect('/')   
    else:
        f=IncomeForm
        context={'form':f}
        return render(request,'addincome.html',context)



def income_list(request):
        # uid=request.session.get('uid')
        # #incl=Income.objects.all()
        # incl=Income.objects.filter(user=uid) 
        # context={'incl':incl}
        # return render(request,'incomelist.html',context)


        uid=request.session.get('uid')
        #incl=Income.objects.all()
        incl=Income.objects.filter(user=uid)
        inct=set()
        for i in incl:
             inct.add(i.income_type)
        context={'incl':incl,'inct':inct}
        return render(request,'incomelist.html',context)




def inc_search(request):
     uid=request.session.get('uid')
     srch=request.POST.get('srch')
     incl=Income.objects.filter(user=uid,description__contains=srch)
     context={'incl':incl}
     return render(request,'incomelist.html',context)



def sort_by_income_type(request,inct2):
    uid=request.session.get('uid')
    #incl=Income.objects.all()
    incl=Income.objects.filter(user=uid)
    inct=set()
    for i in incl:
        inct.add(i.income_type)
        expl=Income.objects.filter(user=uid,income_type=inct2)
    context={'incl':incl,'inct':inct}
    return render(request,'incomelist.html',context)







def delete_l(request,icid):
    ic=Income.objects.get(id=icid)
    ic.delete()
    return redirect('/exp_list')



def edit_l(request,icid):
    ic=Income.objects.get(id=icid)
    if request.method=='POST':
        f=IncomeForm(request.POST,instance=ic)
        f.save()
        return redirect('/exp_list')
    else:
        f=IncomeForm(instance=ic)
        context={'form':f}
        return render(request,'addincome.html',context)
      
 