from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
    return render(request, 'TinDevApp/login.html')



def new_user(request):
    return render(request, 'TinDevApp/user_create.html')
