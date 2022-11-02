from django.urls import path
from pedulee.views import BloodView, ClothesView, HistoryView, HomeViews, ProjectView, UserViews, VolunteerView, MoneyView, GroceriesView

app_name = 'pedulee'

home_urls = [
    path('', HomeViews.index, name='home'),
    path('home', HomeViews.index, name='home'),
    path('sign-up/', UserViews.register, name='register'),
    path('sign-in/', UserViews.login, name='login'),
    path('sign-out/', UserViews.logout, name='logout'),
    path('profile/', UserViews.profile, name='profile'),
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
    path('history/volunteer/<int:i>/delete', VolunteerView.delete, name="delete_volunteer")
]

money_urls = [
    path('money/create', MoneyView.create, name='create_money'),
    path('history/money/json', MoneyView.show_json, name='show_json_money'),
    path('history/money/<str:pk>/delete', MoneyView.delete, name='delete_money')
]

grocery_urls = [
    path('groceries/create', GroceriesView.create, name='create_groceries'),
    path('history/api/groceries/', GroceriesView.show_json, name='show_json_groceries'),
    path('groceries/', GroceriesView.show, name='show_groceries'),
    path('history/groceries/<int:i>/delete', GroceriesView.delete, name="delete_groceries")
]

blood_urls = [
     path('blood/create',BloodView.show_blood, name='show_blood'),
     path('api/blood/', BloodView.get_show_blood, name='get_show_blood'),
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