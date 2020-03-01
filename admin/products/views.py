from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def addProduct(request, *args,**kwargs):
    return render(request, "addProduct.html",{})

@login_required
def addP(request, *args,**kwargs):
    if request.method == "POST":
        title = request.POST['title']
        code = request.POST['code']
        price = request.POST['price']
        category = request.POST['category']
        files = request.FILES['file']
        #print("======================="+file.name)
        description = request.POST['description']
        # saving in the db
        p = Product()
        p.name = title
        p.code = code
        p.price = price
        p.category = category
        p.description = description
        p.rates = 4
        p.picture = files
        p.save()
        return render(request, "addProduct.html",{'file':files.name})
    else:
        print("asdjasd")
        
@login_required
def showProducts(request, *args,**kwargs):
    # if we have to remove somthing with 
    if request.method ==  "GET" and request.GET.get('code') :
        #print("--------------------"+ str(request.GET.get('code')))
        code = request.GET.get('code')
        instance = Product.objects.get(code=code)
        instance.delete()
        #print(instance.price)
    proList = Product.objects.all()
    return render(request, "showProducts.html",{'proList':proList})

def showHome(request, *args,**kwargs):
    return render(request, "index.html",{}) 
