from django.urls import path
from pedulee.views import ClothesView, DonateView, HistoryView, HomeViews, ProjectView, UserViews

app_name = 'pedulee'

home_urls = [
    path('', HomeViews.index, name='home'),
    path('home', HomeViews.index, name='home'),
    path('sign-up/', UserViews.register, name='register'),
    path('sign-in/', UserViews.login, name='login'),
    path('sign-out/', UserViews.logout, name='logout'),
]


history_urls = [
    path('history/', HistoryView.show_history, name='history'),
    path('history/clothes', HistoryView.show_clothes_history, name='clothes_history'),
    path('history/money', HistoryView.show_money_history, name='money_history'),
    path('history/groceries', HistoryView.show_groceries_history, name='groceries_history'),
    path('history/blood', HistoryView.show_blood_history, name='blood_history'),
    path('history/volunteer', HistoryView.show_volunteer_history, name='volunteer_history'),
]

cloth_urls = [
    path('json-cloth/', ClothesView.show_json_cloth, name='show_json_cloth'),
    path('clothes/', ClothesView.create_cloth, name='create_cloth'),
    path('clothes/<int:i>/delete', ClothesView.delete, name="delete_cloth")
]

projects_urls = [
    path('projects/', ProjectView.show_projects, name='projects'),
]

urlpatterns = [
    *home_urls,
    *history_urls,
    *cloth_urls,
    *projects_urls,
]