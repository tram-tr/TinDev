from django.urls import path
from . import views
app_name = "TinDevApp"
urlpatterns = [
    path('', views.index, name='index'),
]