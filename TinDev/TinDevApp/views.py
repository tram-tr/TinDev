from django.shortcuts import render

def index(request):
    return render(request, 'TinDevApp/index.html')

def new_user(request):
    return render(request, 'TinDevApp/user_create.html')
