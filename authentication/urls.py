from django.urls import path
from .views import login, logout, register

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='loginflutter'),
    path('logout/', logout, name='logoutflutter'),
    path('register/', register, name='registerflutter'),
]