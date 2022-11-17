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
    path('recruiter/home/<slug:name>/post/view/all', views.PostViewRecruiterAll, name = 'postViewAll'),
    path('recruiter/home/<slug:name>/post/view/active', views.PostViewRecruiterActive, name = 'postViewActive'),
    path('recruiter/home/<slug:name>/post/view/inactive', views.PostViewRecruiterInactive, name = 'postViewInactive'),
    path('recruiter/home/<slug:name>/post/view/applicant', views.PostViewRecruiterApplicant, name = 'postViewApplicant'),

    path('recruiter/home/<slug:name>/post/delete/<int:id_num>', views.PostDeleteRecruiter, name = 'postDelete'),

    path('candidate/home/<slug:name>/post/view/all', views.PostViewCandidateAll, name = 'CandidateView'),
    path('candidate/home/<slug:name>/post/view/active', views.PostViewCandidateActive, name = 'CandidateViewActive'),
    path('candidate/home/<slug:name>/post/view/inactive', views.PostViewCandidateInactive, name = 'CandidateViewInactive'),


    path('candidate/home/<slug:name>/post/<int:id_num>/apply', views.CandidateApply, name = 'CandidateApply'),
    path('candidate/home/<slug:name>/post/<int:id_num>/unapply', views.CandidateRemoveApplication, name = 'CandidateUnapply'),

    path('candidate/home/<slug:name>/application/view', views.CandidateViewApplication, name = 'ApplicationView'),

    
]
