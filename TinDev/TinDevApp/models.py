from django.db import models
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


class Candidate(models.Model):
    name = models.CharField(max_length=30)

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    years = models.IntegerField()
    zipcode = models.IntegerField()

    skills = models.CharField(max_length=500)

    def get_absolute_url(self):
        redirect('login')
    

class Recruiter(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    zipcode  = models.IntegerField()
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length=30)

    def get_absolute_url(self):
        redirect('login/')
