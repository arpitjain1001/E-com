from django.http import HttpResponse
from django.shortcuts import render
from . models import Product
from math import ceil

# Create your views here.
def admin(request):
    return HttpResponse("<h1>HELLO SIR !!</h1>")
 
def index(request):
    products = Product.objects.all()
    # print(products)
    # n=len(products)
    # nslides = n//4 + ceil(n//4-(n//4))
    # context = {'products':prod, 'range':range(nslides),'no_of_slides':nslides}
    # return render(request , "index.html",{'product':products, 'range':range(1,nslides),'no_of_slides':nslides})
    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod =Product.objects.filter(category=cat)
        n= len(prod)
        nslides = n//4 + ceil(n//4-(n//4))
        allprods.append([prod , range(1 , nslides) , nslides])
        context = {'allprods':allprods}
    return render(request , "index.html", context)

def about(request):
    return render(request,"about.html")

def contact(request):
   return render(request,"contact.html")


def tracker(request):
     return render(request,"tracker.html")           

def search(request):
     return render(request,"search.html")


def prodview(request , myid):
     product = Product.objects.filter( id = myid)
     print(product)
     return render(request,"prodview.html",{product:product[0]})


def checkout(request):
    return render(request,"checkout.html")        