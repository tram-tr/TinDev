from django.urls import path
from . import views

app_name = "TinDev"
urlpatterns = [
    path('candidate/login/', views.candidateLoginPage, name='candidate-login'),
    path('recruiter/login/', views.recruiterLoginPage, name='recruiter-login'),

    path('recruiter/home/<slug:name>', views.RecruiterPage, name='recruiter-home'),
    path('candidate/home/<slug:name>', views.CandidatePage, name='candidate-home'),

    path('candidate/add/', views.CandidateCreateView, name='candidateAdd'),
    path('recruiter/add/', views.RecruiterCreateView, name='recruiterAdd'),

    path('recruiter/home/<slug:name>/post/add', views.PostCreateView.as_view(), name = 'postAdd'),
    path('recruiter/home/<slug:name>/post/view/all', views.PostViewRecruiterAll, name = 'postViewAll'),
    path('recruiter/home/<slug:name>/post/view/active', views.PostViewRecruiterActive, name = 'postViewActive'),
    path('recruiter/home/<slug:name>/post/view/inactive', views.PostViewRecruiterInactive, name = 'postViewInactive'),
    path('recruiter/home/<slug:name>/post/view/applicant', views.PostViewRecruiterApplicant, name = 'postViewApplicant'),
    path('recruiter/home/<slug:name>/post/update/<int:id_num>', views.PostUpdateRecruiter, name = 'postUpdate'),
    path('recruiter/home/<slug:name>/post/delete/<int:id_num>', views.PostDeleteRecruiter, name = 'postDelete'),

    path('candidate/home/<slug:name>/post/view/active', views.PostViewCandidateActive, name = 'CandidateViewActive'),
    path('candidate/home/<slug:name>/post/view/inactive', views.PostViewCandidateInactive, name = 'CandidateViewInactive'),
    path('candidate/home/<slug:name>/post/view/search/description', views.PostViewCandidateSearchDescription, name = 'CandidateSearchDescription'),
    path('candidate/home/<slug:name>/post/view/search/zipcode', views.PostViewCandidateSearchZipCode, name = 'CandidateSearchZipcode'),



    path('candidate/home/<slug:name>/post/<int:id_num>/apply', views.CandidateApply, name = 'CandidateApply'),
    path('candidate/home/<slug:name>/post/<int:id_num>/unapply', views.CandidateRemoveApplication, name = 'CandidateUnapply'),

    path('candidate/home/<slug:name>/application/view', views.CandidateViewApplication, name = 'ApplicationView'),

    
]
