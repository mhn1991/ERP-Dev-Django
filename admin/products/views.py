from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from .models import Product,Images,Category,RateComments,Template
from django.shortcuts import redirect
from django.http import HttpResponse,JsonResponse
import json

@login_required
def addProduct(request, *args,**kwargs):
    cats = Category.objects.all()
    templates = Template.objects.all()
    return render(request, "addProduct.html",{'cats':cats,'templates':templates})


@login_required
def getTemplate(request, *args,**kwargs):
    if request.method == "POST":
        name = request.POST['name']
        template = Template.objects.values('content').get(name=name)
        return JsonResponse(template['content'])


@login_required
def addP(request, *args,**kwargs):
    if request.method == "POST":
        title = request.POST['title']
        code = request.POST['code']
        price = request.POST['price']
        number = request.POST['number']
        category = request.POST['category']
        discount = request.POST['discount']
        files = request.FILES.getlist('file')
        description = request.POST['description']
        user = request.user.username
        discountStartDate = request.POST['startDate']
        discountEndDate = request.POST['endDate']
        template = request.POST['template']
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
        p.number = number
        p.discount = discount
        p.discountStartDate = discountStartDate
        p.discountEndDate = discountEndDate
        p.information = Template.objects.get(name=template)
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


@login_required
def addtemplate(request, *args,**kwargs):
    if request.method ==  "GET":
        return render(request, "templateManagment.html",{})
    elif request.method == "POST":
        data = json.loads(request.body)
        data.pop(0)
        name = data[0]['value']
        data.pop(0)
        final = {}
        # make final json file to store in the db 
        for i in range(len(data)):
            if i%2 == 0:
                key = data[i]['name']
                value = data[i+1]['name']
                final[key] = value
        instance = Template(name=name, content=final)
        instance.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)



#show products
def showProductsClient(request, *args,**kwargs):
    proList = Product.objects.all()
    return render(request, "product.html",{'proList':proList})

#product page todo!
def showProductPage(request, *args,**kwargs):
    if request.method == "GET":
        code     = request.GET.get('code')
        images   = Images.objects.filter(code=code)
        products = Product.objects.get(code=code)
        comments = RateComments.objects.filter(product=code)
        #print(products.information.content)
    return render(request, "product_detail.html",{'images':images,
                                                  'product':products,
                                                  'comments':comments})


def saveReview(request, *args,**kwargs):
    if request.method == "POST":
        code    = request.POST['code']
        product = Product.objects.get(code=code)
        name    = request.POST['user']
        title   = request.POST['title']
        comment = request.POST['comment']
        rate    = request.POST['rate']
        
    instance = RateComments(product=product,name=name,title=title,rate=0,comment=comment)
    instance.save()
    return redirect("/productDetail/?code="+code)
        
def showHome(request, *args,**kwargs):
    return render(request, "index.html",{}) 
