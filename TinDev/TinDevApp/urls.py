from django.urls import path
from . import views
app_name = "TinDev"
urlpatterns = [
    path('', views.index, name='index'),
]