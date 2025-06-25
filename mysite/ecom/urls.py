# from django.urls import path
# from ecom.views import index, contacts


# urlpattrens = [
#     path("hello/", index),
#     path("contacts/", contacts)
# ]

from django.urls import path
from ecom.views import index, indexItem, add_item, update_item, delete_item

app_name = 'ecom'

urlpatterns = [
    path('', index,name='index'),
    path('<int:My_id>/', indexItem, name='detail'),
    path('additem/', add_item, name='add_item'),
    path('updateitem/<int:My_id>/', update_item, name='update_item'),
    path('deleteitem/<int:My_id>/', delete_item, name='delete_item'),
]