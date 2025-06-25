# from django.urls import path
# from ecom.views import index, contacts


# urlpattrens = [
#     path("hello/", index),
#     path("contacts/", contacts)
# ]

from django.urls import path
from .views import register,profile
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'ecom'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),

]