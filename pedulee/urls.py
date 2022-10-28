from django.urls import path
from pedulee.views import register
from pedulee.views import login_user
from pedulee.views import logout_user
from pedulee.views import show_home

app_name = 'pedulee'

urlpatterns = [
    path('', show_home, name='home'),
    path('home', show_home, name='home'),
    path('sign-up/', register, name='register'),
    path('sign-in/', login_user, name='login'),
    path('sign-out/', logout_user, name='logout'),
    
]