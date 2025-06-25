# from django.urls import path
# from ecom.views import index, contacts


# urlpattrens = [
#     path("hello/", index),
#     path("contacts/", contacts)
# ]

from django.urls import path
from ecom.views import index, indexItem, add_item

app_name = 'ecom'

urlpatterns = [
    path('', index),
    path('<int:My_id>/', indexItem, name='detail'),
    path('additem/', add_item, name='add_item'),
]