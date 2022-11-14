from django.urls import path
from . import views

app_name = "TinDev"
urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('candidate/add/', views.CandidateCreateView.as_view(), name='candidate-add'),
    path('recruiter/add/', views.RecruiterCreateView.as_view(), name='recruiter-add'),
]
