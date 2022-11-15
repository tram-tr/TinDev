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
                response = redirect(reverse('TinDevApp:home'))
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
                response = redirect(reverse('TinDevApp:home'))
                return response
            else:
                message = 'Login Failed'

    return render(request, 'TinDevApp/recruiterlogin.html', context={'form': form, 'message':message})

def homePage(request):
    return render(request, 'TinDevApp/home.html')

class CandidateCreateView(CreateView):
    model = Candidate
    fields = ['name', 'username', 'password', 'years', 'zipcode', 'skills']

class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = ['name', 'company', 'zipcode', 'username', 'password']
