from django.urls import path
from pedulee.views import signup
from pedulee.views import signin_user
from pedulee.views import signout_user

app_name = 'pedulee'

urlpatterns = [
    path('sign-up/', signup, name='signup'),
    path('sign-in/', signin_user, name='signin'),
    path('sign-out/', signout_user, name='signout'),
]