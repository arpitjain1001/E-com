from django.db import models

# Create your models here.
# product jo h vo database h yaha pae
# class Product (models.Model):
#     # product_id = models.AutoField
#     product_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50,default="")
#     subcategory = models.CharField(max_length=50)
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     pub_date = models.DateField()
    # image = models.ImageField(upload_to='shop/images',default="")

#     def __str__(self):
#         return self.product_name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(null=True,blank=True,max_length=50)
    subcategory = models.CharField(null=True,blank=True,max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images',null=True,blank=True)


    def __str__(self):
        return self.product_name



# yeh sb shell(terminal) mae krne h
# python manage.py shell
# from shop.models import Product
# products.objects.all()
# myprod=Product(product_name="mouse")
# from django.utils import timezone
# myprod.save()
# myprod.product_name
