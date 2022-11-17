from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from TinDevApp.models import *
from . import forms
from django.shortcuts import redirect
from django.db.models import F


def redirect_view(request, url):
    response = redirect(url)
    return response

def candidateLoginPage(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = Candidate.objects.filter(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                message = f'Hello {user[0].name}'
                response = redirect(reverse('TinDevApp:candidate-home',kwargs={'name':user[0].username}))
                return response
            else:
                message = f'Login Failed'
                
                
    return render(request, 'TinDevApp/candidatelogin.html', context={'form': form, 'message':message})

def recruiterLoginPage(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = Recruiter.objects.filter(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                message = f'Hello {user[0].name}'
                response = redirect(reverse('TinDevApp:recruiter-home', kwargs={'name':user[0].username}))
                return response
            else:
                message = 'Login Failed'

    return render(request, 'TinDevApp/recruiterlogin.html', context={'form': form, 'message':message})

def RecruiterPage(request, name):
    return render(request, 'TinDevApp/recruiter_home.html', {'name':name})

def CandidatePage(request, name):
    return render(request, 'TinDevApp/candidate_home.html', {'name': name})

class CandidateCreateView(CreateView):
    model = Candidate
    fields = ['name', 'username', 'password', 'years', 'zipcode', 'skills']

class RecruiterCreateView(CreateView):
    model = Recruiter
    fields = ['name', 'company', 'zipcode', 'username', 'password']


# Creating/Editing/Deleting Posts # 

class PostCreateView(CreateView):
    model = Post
    fields = ['recruiter_username', 'position', 'company','location', 'skills', 'description', 'expiration_date', 'pos_type', 'active']

class PostUpdateView(CreateView):
    model = Post
    fields = ['recruiter_username', 'position', 'location', 'skills', 'description', 'expiration_date', 'pos_type', 'active']
    template_name_suffix = '_update_form'

# View Posts for Recruiter #

def PostViewRecruiterAll(request, name):
    post_list = Post.objects.filter(recruiter_username=name)
    return render(request, 'TinDevApp/recruiter_view_post.html', {'list':post_list, 'name':name, 'active':'All'})
def PostViewRecruiterActive(request, name):
    post_list = Post.objects.filter(recruiter_username=name,active='A')
    return render(request, 'TinDevApp/recruiter_view_post.html', {'list':post_list, 'name':name, 'active':'Active'})
def PostViewRecruiterInactive(request, name):
    post_list = Post.objects.filter(recruiter_username=name,active='I')
    return render(request, 'TinDevApp/recruiter_view_post.html', {'list':post_list, 'name':name, 'active':'Inactive'})
def PostViewRecruiterApplicant(request, name):
    post_list = list(Post.objects.all())
    post_list = [x for x in post_list if x.applicant_count > 0]
    return render(request, 'TinDevApp/recruiter_view_post.html', {'list':post_list, 'name':name, 'active':'Applicant-Filled'})
def PostDeleteRecruiter(request, name, id_num):
    post = Post.objects.filter(id=id_num)
    post.delete()
    application = Application.objects.filter(job_num=id_num)
    for element in application:
        element.delete()
    return render(request, 'TinDevApp/recruiter_home.html', {'name':name} )


# View Posts of Candidate #
def PostViewCandidateAll(request, name):
    application_list = list(Application.objects.filter(candidate_username=name).values_list('job_num',flat=True))
    post_list = list(Post.objects.all())
    applied_list = [x for x in post_list if x.id in application_list]
    post_list = [x for x in post_list if x not in applied_list]

    return render(request, 'TinDevApp/candidate_view_post.html', {'post_list':post_list, 'apply_list': applied_list, 'name':name, 'active':'All'})
def PostViewCandidateActive(request, name):
    application_list = Application.objects.filter(candidate_username=name).values_list('job_num',flat=True)
    post_list = list(Post.objects.filter(active='A'))
    applied_list = [x for x in post_list if x.id in application_list]
    post_list = [x for x in post_list if x not in applied_list]

    return render(request, 'TinDevApp/candidate_view_post.html', {'post_list':post_list, 'apply_list': applied_list, 'name':name, 'active':'Active'})

def PostViewCandidateInactive(request, name):
    application_list = Application.objects.filter(candidate_username=name).values_list('job_num',flat=True)
    post_list = list(Post.objects.filter(active='I'))
    applied_list = [x for x in post_list if x.id in application_list]
    post_list = [x for x in post_list if x not in applied_list]
    return render(request, 'TinDevApp/candidate_view_post.html', {'post_list':post_list, 'apply_list': applied_list, 'name':name, 'active':'Active'})



# Applications #

#Application Add/Delete #

def CandidateApply(request, name, id_num):
    apply = Application.objects.filter(candidate_username=name, job_num=id_num)
    if (len(apply) == 0):
        candidate = Candidate.objects.filter(username=name)
        post = Post.objects.filter(id=id_num)
        post.update(applicant_count=F('applicant_count') + 1)


        application = Application(job_num=id_num, candidate_name=candidate[0].name, candidate_username=name,status='APLY',job_title=post[0].position, job_company=post[0].company)
        application.save()

    return render(request, 'TinDevApp/candidate_apply_post.html', {'name':name})

def CandidateRemoveApplication(request, name, id_num):
    apply = Application.objects.filter(candidate_username=name, job_num=id_num)
    apply[0].delete()
    post = Post.objects.filter(id=id_num)
    post.update(applicant_count=F('applicant_count') - 1)

    return render(request, 'TinDevApp/candidate_apply_post.html', {'name':name})

#Application View

def CandidateViewApplication(request, name):
    apply = Application.objects.filter(candidate_username=name)

    return render(request, 'TinDevApp/candidate_view_applications.html', {'list':apply, 'name':name})










