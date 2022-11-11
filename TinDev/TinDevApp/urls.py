from django.urls import path
from . import views
app_name = "TinDev"
urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('createuser/' , views.new_user, name='new_user'),
]
