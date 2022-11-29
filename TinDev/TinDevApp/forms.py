from django import forms
from TinDevApp.models import *

# New Candidate Form
class CandidateRegisterForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'username', 'password', 'zipcode', 'skills', 'years']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'zipcode' : forms.NumberInput(attrs={'placeholder': 'Zip Code'}),
            'skills': forms.TextInput(attrs={'placeholder': 'List of Skills'}),
            'years' :  forms.NumberInput(attrs={'placeholder': 'Years of Experience'}),
        }
        labels = dict.fromkeys(fields, '')

# New Recruiter Form
class RecruiterRegisterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ['name', 'company', 'username', 'password', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'zipcode' : forms.NumberInput(attrs={'placeholder': 'Zip Code'}),
        }
        labels = dict.fromkeys(fields, '')

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username'}), label=False)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label=False)

# Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['position', 'location', 'company', 'skills', 'description', 'expiration_date', 'pos_type', 'active']
        labels = {
            'location': 'Location (City, State)',
            'skills': 'List of Skills',
            'expiration_date': 'Expiration Date (yyyy/mm/dd)',
            'pos_type': 'Position Type',
            'active': 'Status',
        }

class Offer(forms.ModelForm):
    class Meta:
            model = Offer
            fields = ['yearly_salary', 'expiration_date']
            labels = {
                'yearly_salary': 'Yearly Salary',
                'expiration_date': 'Expiration Date (yyyy/mm/dd)'
            }
            