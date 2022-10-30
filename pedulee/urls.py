from django.urls import path
from pedulee.views import ClothesView, HistoryView, HomeViews, ProjectView, UserViews, VolunteerView

app_name = 'pedulee'

home_urls = [
    path('', HomeViews.index, name='home'),
    path('home', HomeViews.index, name='home'),
    path('sign-up/', UserViews.register, name='register'),
    path('sign-in/', UserViews.login, name='login'),
    path('sign-out/', UserViews.logout, name='logout'),
    path('profile/', UserViews.profile, name='profile')
]


history_urls = [
    path('history/', HistoryView.show_history, name='history'),
    path('history/clothes', HistoryView.show_clothes, name='clothes_history'),
    path('history/money', HistoryView.show_money, name='money_history'),
    path('history/groceries', HistoryView.show_groceries, name='groceries_history'),
    path('history/blood', HistoryView.show_blood, name='blood_history'),
    path('history/volunteer', HistoryView.show_volunteer, name='volunteer_history'),
]

cloth_urls = [
    path('json-cloth/', ClothesView.show_json, name='show_json_cloth'),
    path('cloth/', ClothesView.show, name='show_cloth'),
    path('cloth/create', ClothesView.create, name='create_cloth'),
    path('cloth/<int:i>/delete', ClothesView.delete, name="delete_cloth")
]

projects_urls = [
    path('projects/', ProjectView.show, name='projects'),
]

volunteers_urls = [
    path('volunteer/', VolunteerView.create, name='create_volunteer'),
]

urlpatterns = [
    *home_urls,
    *history_urls,
    *cloth_urls,
    *projects_urls,
    *volunteers_urls,
]