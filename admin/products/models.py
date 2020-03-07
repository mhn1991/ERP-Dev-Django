from django.db import models


def upload_location(instance,filename):
    return "%s/%s" %(instance.code,filename)


class Category(models.Model):
    category = models.TextField(primary_key=True)

# Create your models here.
class Product(models.Model):
    name        = models.TextField(blank=True,null=True)
    code        = models.CharField(max_length=1024,primary_key=True)
    picture     = models.ImageField(upload_to=upload_location,null=True,blank=True)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=1000)
    summary     = models.TextField(blank=True,null=True)
    category    = models.ForeignKey(Category,on_delete=models.CASCADE)
    Author      = models.TextField(blank=True,null=True)
    edited      = models.DateField(auto_now_add=True)
    editor      = models.TextField(blank=True,null=True)
    comments    = models.TextField(blank=True,null=True)
    rates       = models.DecimalField(decimal_places=1,max_digits=2)

    def __str__(self):
        return self.code

    
class Images(models.Model):
    code = models.ForeignKey(Product,on_delete=models.CASCADE)
    img = models.ImageField(upload_to=upload_location,null=True,blank=True)
