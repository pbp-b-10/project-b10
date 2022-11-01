from django.urls import path
from pedulee.views import register
from pedulee.views import login_user
from pedulee.views import logout_user
from pedulee.views import show_home
from pedulee.views import show_history
from pedulee.views import show_clothes_history
from pedulee.views import show_money_history
from pedulee.views import show_groceries_history
from pedulee.views import show_blood_history
from pedulee.views import show_volunteer_history
from pedulee.views import show_json_cloth
from pedulee.views import create_cloth
from pedulee.views import show_projects
from pedulee.views import show_blood

app_name = 'pedulee'

urlpatterns = [
    path('', show_home, name='home'),
    path('home', show_home, name='home'),
    path('history', show_history, name='history'),
    path('clothes-history', show_clothes_history, name='clothes_history'),
    path('money-history', show_money_history, name='money_history'),
    path('groceries-history', show_groceries_history, name='groceries_history'),
    path('blood-history', show_blood_history, name='blood_history'),
    path('volunteer-history', show_volunteer_history, name='volunteer_history'),
    path('projects/', show_projects, name='projects'),
    path('sign-up/', register, name='register'),
    path('sign-in/', login_user, name='login'),
    path('sign-out/', logout_user, name='logout'),
    path('json-cloth/', show_json_cloth, name='show_json_cloth'),
    path('clothes/', create_cloth, name='create_cloth'),
    path('blood-donors/',show_blood, name='show_blood'),
]