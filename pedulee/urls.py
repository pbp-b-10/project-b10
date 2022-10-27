from django.urls import path
from pedulee.views import register
from pedulee.views import login_user
from pedulee.views import logout_user

app_name = 'pedulee'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]