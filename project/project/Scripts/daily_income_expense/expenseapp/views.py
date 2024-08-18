from django.shortcuts import render,redirect
from .models import ExpenseForm,Expense

# Create your views here.
from django.contrib.auth.models import User


def add_expense(request):
    uid=request.session.get('uid')
    if request.method=='POST':
        #f=ExpenseForm(request.POST)
        expense=request.POST.get('expense')  
        expense_type=request.POST.get('expense_type')  
        expense_date=request.POST.get('expense_date')  
        description=request.POST.get('description') 
        exp=Expense()
        exp.expense=expense 
        exp.expense_type=expense_type 
        exp.expense_date=expense_date 
        exp.description=description
        exp.user=User.objects.get(id=uid)
        exp.save()
        return redirect('/')
    else:
        f=ExpenseForm
        context={'form':f}
        return render(request,'addexpense.html',context)
    


    
def expense_list(request):
    # uid=request.session.get('uid')
    # #expl=Expense.objects.all()
    # expl=Expense.objects.filter(user=uid)
    # context={'expl':expl}
    # return render(request,'expenselist.html',context)

    uid=request.session.get('uid')
    #expl=Expense.objects.all()
    expl=Expense.objects.filter(user=uid)
    expt=set()
    for i in expl:
        expt.add(i.expense_type)
    context={'expl':expl,'expt':expt}
    return render(request,'expenselist.html',context)




def exp_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    expl=Expense.objects.filter(user=uid,description__contains=srch)
    context={'expl':expl}
    return render(request,'expenselist.html',context)



def sort_by_expense_type(request,ext2):
    uid=request.session.get('uid')
    #expl=Expense.objects.all()
    expl=Expense.objects.filter(user=uid)
    expt=set()
    for i in expl:
        expt.add(i.expense_type)
        expl=Expense.objects.filter(user=uid,expense_type=ext2)
    context={'expl':expl,'expt':expt}
    return render(request,'expenselist.html',context)



    

def delete_l(request,exid):
    ex=Expense.objects.get(id=exid)
    ex.delete()
    return redirect('/exp_list')



def edit_l(request,exid):
    ex=Expense.objects.get(id=exid)
    if request.method=='POST':
        f1=ExpenseForm(request.POST,instance=ex)
        f1.save()
        return redirect('/exp_list')
    else:
        f=ExpenseForm(instance=ex)
        context={'form':f}
        return render(request,'addexpense.html',context)
      
     
     
     


     




