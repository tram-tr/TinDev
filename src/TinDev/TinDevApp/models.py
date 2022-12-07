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
    username = models.CharField(max_length = 30, unique=True)
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
    job = models.ForeignKey(Post, related_name='applications', on_delete=models.CASCADE, null=True)

    candidate_username = models.CharField(max_length=30, default='')
    candidate = models.ForeignKey(Candidate, related_name='applications', on_delete=models.CASCADE, null=True)
    
    offer_expire = models.DateField(default=datetime.date.today)
    APLY = 'APLY'
    REJT = 'REJT'
    ACCT = 'ACCT'
    EXND = 'EXND'
    EXPR = 'EXPR'
    POSITION_TYPE_CHOICES = [
        (APLY, 'Applied/Pending'),
        (REJT, 'Rejected'),
        (ACCT, 'Accepted'),
        (EXND, 'Offer Extended'),
        (EXPR, 'Expired')
    ]

    status = models.CharField(
        max_length=4,
        choices=POSITION_TYPE_CHOICES,
        default=APLY,
    )

    # calculate compatibility score
    def compatibility_score(self):
        score = 0

        job_skills = self.job.skills.lower()
        candidate_skills = self.candidate.skills.lower()

        # if candidate has no skill return 0
        if len(candidate_skills) == 0:
            return 0

        # score = similarity between two strings
        job_skills = job_skills + ' ' * (len(candidate_skills) - len(job_skills))
        candidate_skills = candidate_skills + ' ' * (len(job_skills) - len(candidate_skills))

        score = sum(1 if i == j else 0 for i, j in zip(job_skills, candidate_skills)) / float(len(job_skills))
        return round(score * 100, 2)

class NotInterest(models.Model):
    job_num = models.IntegerField()
    candidate_username = models.CharField(max_length=30, default='')

class Offer(models.Model):
    app_id = models.ForeignKey(Application, related_name='offers', on_delete=models.CASCADE, null=True)
    yearly_salary = models.IntegerField()
    expiration_date = models.DateField()

