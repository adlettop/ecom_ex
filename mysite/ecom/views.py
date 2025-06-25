from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    items = Product.objects.all()
    context = {
        'items':items
    }
    return render(request, 'ecom/index.html',context)

def indexItem(request, My_id):
    item = Product.objects.get(id=My_id)
    context = {
        'item':item
    }
    return render(request,"ecom/detail.html", context=context)

def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get('upload')
        item = Product(name=name,price=price,description=description, image=image)
        item.save()
    return render(request,'ecom/additem.html')

