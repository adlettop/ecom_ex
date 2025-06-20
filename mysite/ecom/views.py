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

