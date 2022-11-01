from django.urls import path
from pedulee.views import ClothesView, HistoryView, HomeViews, ProjectView, UserViews, VolunteerView, MoneyView

app_name = 'pedulee'

home_urls = [
    path('', HomeViews.index, name='home'),
    path('home', HomeViews.index, name='home'),
    path('sign-up/', UserViews.register, name='register'),
    path('sign-in/', UserViews.login, name='login'),
    path('sign-out/', UserViews.logout, name='logout'),
    path('profile/', UserViews.profile, name='profile'),
    path('about/', UserViews.profile, name='about')
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
    path('history/api/cloth/', ClothesView.show_json, name='show_json_cloth'),
    path('cloth/', ClothesView.show, name='show_cloth'),
    path('cloth/create', ClothesView.create, name='create_cloth'),
    path('history/cloth/<int:i>/delete', ClothesView.delete, name="delete_cloth")
]

projects_urls = [
    path('projects/', ProjectView.show, name='projects'),
]

volunteers_urls = [
    path('volunteer/create', VolunteerView.create, name='create_volunteer'),
    path('api/volunteer/', VolunteerView.show_json, name='show_json_volunteer'),
]

money_urls = [
    path('money/create', MoneyView.show, name='create_money'),
]

grocery_urls = [
    path('grocery/create', VolunteerView.create, name='create_groceries'),
]

blood_urls = [
    path('blood/create', VolunteerView.create, name='create_blood'),
]

urlpatterns = [
    *home_urls,
    *history_urls,
    *cloth_urls,
    *projects_urls,
    *volunteers_urls,
    *money_urls,
    *grocery_urls,
    *blood_urls,
]