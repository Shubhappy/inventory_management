from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .forms import vendor_group_registration, vendor_group_update
from .models import customerrole
import datetime
import xlwt
from 

def home_view (request):
    context= {'mytime':datetime.datetime.now()}
    return render (request, 'ecomapp/base.html',context= {'mytime':datetime.datetime.now()})

def dashboard_view (request):
    context= {'mytime':datetime.datetime.now()}
    custno=customerrole.objects.count()
    print(custno)
    return render (request, 'ecomapp/dashboard.html',context= {'mytime':datetime.datetime.now(), 'custno':custno})


# This function will create and retrieve the data
def customer_role_view (request):
    if request.method == 'POST':
        fm = vendor_group_registration(request.POST)
        if fm.is_valid():
            fm.save()
           
            fm=vendor_group_registration()
    else:
        fm=vendor_group_registration()
    cust=customerrole.objects.all()
    
    return render (request, 'ecomapp/customer.html',{'form':fm,'cus':cust})

# This function will edit/update the data
def update_data(request, id):
    if request.method == 'POST':
        pi = customerrole.objects.get(pk=id)
        fm= vendor_group_update(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            fm=vendor_group_update()
    else:
        pi= customerrole.objects.get(pk=id)
        fm= vendor_group_update(instance=pi)
    return render(request, 'ecomapp/update.html', {'form':fm})

# This function will delete the data
def delete_data(request, id):
    if request.method == 'POST':
        pi = customerrole.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/customer')

def products_view (request):
    return render (request, 'ecomapp/products.html')