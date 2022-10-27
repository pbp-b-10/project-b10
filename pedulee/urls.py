from django.urls import path
from pedulee.views import register
from pedulee.views import login_user
from pedulee.views import logout_user
from pedulee.views import show_home

app_name = 'pedulee'

urlpatterns = [
    path('sign-up/', register, name='register'),
    path('sign-in/', login_user, name='login'),
    path('sign-out/', login_user, name='logout'),
    path('home/', show_home, name='home'),
]