from django.db import models
from django.urls import reverse


class Candidate(models.Model):
    name = models.CharField(max_length=30)

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    years = models.IntegerField()
    zipcode = models.IntegerField()

    skills = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('TinDevApp:candidate-login')

class Recruiter(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    zipcode  = models.IntegerField()
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('TinDevApp:recruiter-login')

class Post(models.Model):
    recruiter_username = models.CharField(max_length=30, default='')
    position = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    skills = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    expiration_date = models.DateField()
    


    FULL = 'FULL'
    PART = 'PART'
    POSITION_TYPE_CHOICES = [
        (FULL, 'Full-Time'),
        (PART, 'Part-Time'),
    ]

    pos_type = models.CharField(
        max_length=4,
        choices=POSITION_TYPE_CHOICES,
        default=FULL,
    )


    A = 'A'
    I = 'I'
    POSITION_TYPE_CHOICES = [
        (A, 'Active'),
        (I, 'Inactive'),
    ]

    active = models.CharField(
        max_length=1,
        choices=POSITION_TYPE_CHOICES,
        default=FULL,
    )

    def get_absolute_url(self):
        return reverse('TinDevApp:recruiter-home', kwargs={'name':self.recruiter_username})

    def __str__(self):
        return self.position



