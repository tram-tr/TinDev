from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from TinDevApp.models import *
from . import forms
from django.contrib.auth import login, authenticate

def loginPage(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = Candidate.objects.filter(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                message = f'Hello {user[0].name}'
                
    return render(request, 'TinDevApp/login.html', context={'form': form, 'message':message})

class CandidateCreateView(CreateView):
    model = Candidate
    fields = ['name', 'username', 'password', 'years', 'zipcode', 'skills']

class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = ['name', 'company', 'zipcode', 'username', 'password']
