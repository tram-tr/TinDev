from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=30)

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    years = models.IntegerField()
    zipcode = models.IntegerField()

    skills = models.CharField(max_length=500)
