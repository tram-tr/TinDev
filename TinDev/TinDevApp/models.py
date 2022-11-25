from django.db import models
from django.urls import reverse
import datetime

# Candidate's Model
class Candidate(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    skills = models.CharField(max_length=500)
    years = models.IntegerField()

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('TinDevApp:candidate-login')

# Recruiter's Model
class Recruiter(models.Model):
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    zipcode  = models.IntegerField()
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length=30)

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('TinDevApp:recruiter-login')

class Post(models.Model):
    recruiter_username = models.CharField(max_length=30, default='')
    position = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    skills = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    expiration_date = models.DateField(default=datetime.date.today)
    applicant_count  = models.IntegerField(default=0)

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

class Application(models.Model):
    job_num = models.IntegerField()
    job = models.ForeignKey(Post, related_name='applications', on_delete=models.CASCADE, default='')

    candidate_username = models.CharField(max_length=30, default='')
    candidate_name = models.CharField(max_length=30, default='')
    candidate_year = models.IntegerField(default=0)
    candidate_skill = models.CharField(max_length=500, default='')

    
    APLY = 'APLY'
    REJT = 'REJT'
    ACCT = 'ACCT'
    EXND = 'EXND'
    POSITION_TYPE_CHOICES = [
        (APLY, 'Applied/Pending'),
        (REJT, 'Rejected'),
        (ACCT, 'Accepted'),
        (EXND, 'Offer Extended'),
    ]

    status = models.CharField(
        max_length=4,
        choices=POSITION_TYPE_CHOICES,
        default=APLY,
    )

class NotInterest(models.Model):
    job_num = models.IntegerField()
    candidate_username = models.CharField(max_length=30, default='')


