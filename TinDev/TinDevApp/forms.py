from django import forms
from TinDevApp.models import *

class CandidateRegisterForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'username', 'password', 'zipcode', 'skills', 'years']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'name' : 'Full Name',
            'username' : 'Username',
            'password' : 'Password',
            'password2' : 'Confirm Password',
            'zipcode' : 'Zip Code',
            'skills': 'List of Skills',
            'years' : 'Years of Experience'
        }     

class RecruiterRegisterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ['name', 'company', 'username', 'password', 'zipcode']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'name': 'Full Name',
            'company': 'Company',
            'username': 'Username',
            'password': 'Password',
            'zipcode': 'Zip Code'
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)