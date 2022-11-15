from django.urls import path
from . import views

app_name = "TinDev"
urlpatterns = [
    path('candidatelogin/', views.candidateLoginPage, name='candidate-login'),
    path('recruiterlogin/', views.recruiterLoginPage, name='recruiter-login'),

    path('recruiter/home/<slug:name>', views.RecruiterPage, name='recruiter-home'),
    path('candidate/home/<slug:name>', views.CandidatePage, name='candidate-home'),

    path('candidate/add/', views.CandidateCreateView.as_view(), name='candidateAdd'),
    path('recruiter/add/', views.RecruiterCreateView.as_view(), name='recruiterAdd'),
    path('recruiter/home/<slug:name>/post/add', views.PostCreateView.as_view(), name = 'postAdd'),
    path('recruiter/home/<slug:name>/post/view', views.PostViewRecruiter, name = 'postView'),
]
