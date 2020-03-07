from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from .models import Product,Images,Category

@login_required
def addProduct(request, *args,**kwargs):
    cats = Category.objects.all()
    return render(request, "addProduct.html",{'cats':cats})

@login_required
def addP(request, *args,**kwargs):
    if request.method == "POST":
        title = request.POST['title']
        code = request.POST['code']
        price = request.POST['price']
        category = request.POST['category']
        #pic = request.FILES['file']
        files = request.FILES.getlist('file')
        description = request.POST['description']
        user = request.user.username
        # saving in the db
        p = Product()
        p.name = title
        p.code = code
        p.price = price
        p.category = Category.objects.get(category__exact=category)
        p.description = description
        p.rates = 4
        p.picture = files[0]
        p.editor = user
        p.save()
        for f in files:
            instance = Images(img=f,code=p)
            instance.save()
        return render(request, "addProduct.html",{})
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

#category page
@login_required
def showCategoryManagemet(request, *args,**kwargs):
    return render(request, "categoryManagement.html",{})

@login_required
def addCategory(request, *args,**kwargs):
    if request.method ==  "POST":
        instance = Category(category = request.POST['name'])
        instance.save()
    return render(request, "categoryManagement.html",{})


#show products
def showProductsClient(request, *args,**kwargs):
    proList = Product.objects.all()
    return render(request, "product.html",{'proList':proList})

#product page todo!
def showProductPage(request, *args,**kwargs):
    if request.method == "GET":
        images = Images.objects.filter(code=request.GET.get('code'))
        products = Product.objects.get(code=request.GET.get('code'))
    return render(request, "product_detail.html",{'images':images,'product':products})

def showHome(request, *args,**kwargs):
    return render(request, "index.html",{}) 
