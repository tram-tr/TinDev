from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from TinDevApp.models import *
from . import forms
from django.shortcuts import redirect

def redirect_view(request, url):
    response = redirect(url)
    return response

def candidateLoginPage(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = Candidate.objects.filter(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                message = f'Hello {user[0].name}'
                response = redirect(reverse('TinDevApp:candidate-home',kwargs={'name':user[0].username}))
                return response
            else:
                message = f'Login Failed'
                
                
    return render(request, 'TinDevApp/candidatelogin.html', context={'form': form, 'message':message})

def recruiterLoginPage(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = Recruiter.objects.filter(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                message = f'Hello {user[0].name}'
                response = redirect(reverse('TinDevApp:recruiter-home', kwargs={'name':user[0].username}))
                return response
            else:
                message = 'Login Failed'

    return render(request, 'TinDevApp/recruiterlogin.html', context={'form': form, 'message':message})

def RecruiterPage(request, name):
    return render(request, 'TinDevApp/recruiter_home.html', {'name':name})

def CandidatePage(request, name):
    return render(request, 'TinDevApp/candidate_home.html', {'name': name})

class CandidateCreateView(CreateView):
    model = Candidate
    fields = ['name', 'username', 'password', 'years', 'zipcode', 'skills']

class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = ['name', 'company', 'zipcode', 'username', 'password']

class PostCreateView(CreateView):
    model = Post
    fields = ['recruiter_username', 'position', 'location', 'skills', 'description', 'expiration_date', 'pos_type', 'active']

class PostUpdateView(CreateView):
    model = Post
    fields = ['recruiter_username', 'position', 'location', 'skills', 'description', 'expiration_date', 'pos_type', 'active']
    template_name_suffix = '_update_form'

def PostViewRecruiter(request, name):
    post_list = Post.objects.filter(recruiter_username=name)
    return render(request, 'TinDevApp/recruiter_view_post.html', {'list':post_list, 'name':name})







