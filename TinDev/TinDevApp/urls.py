from django.urls import path
from . import views

app_name = "TinDev"
urlpatterns = [
    path('candidatelogin/', views.candidateLoginPage, name='candidate-login'),
    path('recruiterlogin/', views.recruiterLoginPage, name='recruiter-login'),
    path('home/', views.homePage, name='home'),
    path('candidate/add/', views.CandidateCreateView.as_view(), name='candidateAdd'),
    path('recruiter/add/', views.RecruiterCreateView.as_view(), name='recruiterAdd'),
]
