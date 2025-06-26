from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required

def index(request):
    items = Product.objects.all()
    
    # Поиск
    item_name = request.GET.get("search")
    if item_name:
        items = items.filter(name__icontains=item_name)
    
    # Сортировка
    sort_by = request.GET.get('sort')
    valid_sort_fields = ['price', '-price']
    if sort_by in valid_sort_fields:
        items = items.order_by(sort_by)
    
    context = {
        'items': items,
        'sort_by': sort_by,  # чтобы в шаблоне знать текущий режим сортировки
    }
    return render(request, 'ecom/index.html', context)


# class ProductListView(ListView):
#     model = Product
#     template_name = 'ecom/index.html'
#     context_object_name = "items"

def indexItem(request, My_id):
    item = Product.objects.get(id=My_id)
    context = {
        'item':item
    }
    return render(request,"ecom/detail.html", context=context)

@login_required
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get('upload')
        seller = request.user
        item = Product(name=name,price=price,description=description, image=image, seller=seller)
        item.save()
    return render(request,'ecom/additem.html')

def update_item(request,My_id):
    item = Product.objects.get(id=My_id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get('upload', item.image)
        item.save()
        return redirect("/ecom/")

    context = {
        'item':item
    }
    return render(request,'ecom/updateitem.html', context)


def delete_item(request,My_id):
    item = Product.objects.get(id=My_id)
    if request.method == "POST":
        item.delete()
        return redirect("/ecom/")

    context = {
        'item':item
    }
    return render(request,'ecom/deleteitem.html', context)


