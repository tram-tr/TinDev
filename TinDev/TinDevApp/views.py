from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from TinDevApp.models import *
from . import forms
from django.shortcuts import redirect
from django.db.models import F, Q
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date


def redirect_view(request, url):
    response = redirect(url)
    return response

# Candidate's login page
def candidateLoginPage(request):
    form = forms.LoginForm()
    message = ''

    curr_date = date.today()
    for post in Post.objects.all():
        if post.expiration_date <= curr_date:
            post.active = 'I'
            post.save()

    for offer in Offer.objects.all():
        if offer.expiration_date <= curr_date:
            app = offer.app_id
            if app and app.status == 'EXND':
                app.status = 'REJT'
                app.save()
                offer.delete()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # check if the login succeed
            user = Candidate.objects.filter(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                # mark the user as the current user
                request.session['candidate_user'] = user[0].username
                message = f'Hello {user[0].name}'
                response = redirect(reverse('TinDevApp:candidate-home',kwargs={'name':user[0].username}))
                return response
            else:
                message = f'Login Failed'
    return render(request, 'TinDevApp/candidate_login.html', context={'form': form, 'message':message})

# Recruiter's login page
def recruiterLoginPage(request):
    form = forms.LoginForm()
    message = ''
    curr_date = date.today()

    for post in Post.objects.all():
        if post.expiration_date <= curr_date:
            for application in Application.objects.filter(job=post):
                application.status = 'REJT'
                application.save()
            post.active = 'I'
            post.save()

    for offer in Offer.objects.all():
        if offer.expiration_date <= curr_date:
            app = offer.app_id
            if app and app.status == 'EXND':
                app.status = 'REJT'
                app.save()
                offer.delete()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # check if the login succeed
            user = Recruiter.objects.filter(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user:
                # mark the user as the current user
                request.session['recruiter_user'] = user[0].username
                message = f'Hello {user[0].name}'
                response = redirect(reverse('TinDevApp:recruiter-home', kwargs={'name':user[0].username}))
                return response
            else:
                message = f'Login Failed'
    return render(request, 'TinDevApp/recruiter_login.html', context={'form': form, 'message':message})

# Recruiter's home page
def RecruiterPage(request, name):
    # check if the user is the current user
    if name in request.session['recruiter_user']:
        current_user = request.session['recruiter_user']
    else:
        # if not redirect to recruiter login
        return redirect('TinDevApp:recruiter-login')
    return render(request, 'TinDevApp/recruiter_home.html', {'name':current_user})

# Candidate's home page
def CandidatePage(request, name):
    # check if the user is the current user
    if name in request.session['candidate_user']:
        current_user = request.session['candidate_user']
    else:
        # if not redirect to candidate login
        return redirect('TinDevApp:candidate-login')
    return render(request, 'TinDevApp/candidate_home.html', {'name': current_user})

# Candidate's register page
def CandidateCreateView(request):
    if request.method == 'POST':
        form = forms.CandidateRegisterForm(request.POST)
        if form.is_valid():
            # check if the username already exists
            new_username = form.cleaned_data.get('username')
            if Candidate.objects.filter(username=new_username).count() > 0:
                return HttpResponse('Username already exists.')
            else:
                # save data and redirect to login
                form.save()
                return redirect('TinDevApp:candidate-login')
    else:
        form = forms.CandidateRegisterForm()

    return render(request, 'TinDevApp/candidate_form.html', context={'form': form})

# Recruiter's register page
def RecruiterCreateView(request):
    if request.method == 'POST':
        form = forms.RecruiterRegisterForm(request.POST)
        if form.is_valid():
            # check if the username already exists
            new_username = form.cleaned_data.get('username')
            if Recruiter.objects.filter(username=new_username).count() > 0:
                return HttpResponse('Username already exists.')
            else:
                # save data and redirect to login
                form.save()
                return redirect('TinDevApp:candidate-login')
    else:
        form = forms.RecruiterRegisterForm()
    
    return render(request, 'TinDevApp/recruiter_form.html', context={'form': form})


# Creating/Editing/Deleting Posts # 

# Creating a New Post
def PostCreate(request, name):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            # Automatically update the current username before save form
            new_post.recruiter_username = name
            new_post.save()
            # Redirect to View All Posts
            return redirect(reverse('TinDevApp:postViewAll',kwargs={'name': name}))
    else:
        form = forms.PostForm()
    return render(request, 'TinDevApp/post_form.html', {'form': form, 'name': name})

# Deleting a Post
def PostDeleteRecruiter(request, name, id_num):
    post = Post.objects.filter(id=id_num)
    post.delete()
    application = Application.objects.filter(job_num=id_num)
    for element in application:
        element.delete()
    return redirect(reverse('TinDevApp:postViewAll',kwargs={'name': name}))

# Update a Current Post
def PostUpdateRecruiter(request, name, id_num):
    post = Post.objects.get(id=id_num, recruiter_username=name)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('TinDevApp:postViewAll',kwargs={'name': name}))
    else:
        form = forms.PostForm(instance=post)

    context = {
        'form': form,
        'name': name
    }
    return render(request, 'TinDevApp/post_update.html', context)

# View Posts for Recruiter #

# View All Posts
def PostViewRecruiterAll(request, name):
    post_list = Post.objects.filter(recruiter_username=name)
    return render(request, 'TinDevApp/recruiter_view_post.html', {'list':post_list, 'name':name, 'active':'All'})

# View All Active Posts
def PostViewRecruiterActive(request, name):
    post_list = Post.objects.filter(recruiter_username=name, active='A')
    return render(request, 'TinDevApp/recruiter_view_post.html', {'list':post_list, 'name':name, 'active':'Active'})

# View All Inactive Posts
def PostViewRecruiterInactive(request, name):
    post_list = Post.objects.filter(recruiter_username=name, active='I')
    return render(request, 'TinDevApp/recruiter_view_post.html', {'list':post_list, 'name':name, 'active':'Inactive'})

# View All Jobs' Applicants
def PostViewRecruiterApplicant(request, name, id_num):
    form = forms.Offer()
    applicants = Application.objects.filter(job__in=Post.objects.filter(recruiter_username=name, id=id_num))
    post = Post.objects.get(id=id_num, recruiter_username=name)
    if request.method == 'POST':
        form = forms.Offer(request.POST)
        if form:
            for k, v in request.POST.items():
                if 'applicant_' in k:
                    app_id = v
                    curr_app = Application.objects.get(id=app_id)
                    Application.objects.filter(id=app_id).update(status="EXND")
                    if form.is_valid():
                        new_offer = form.save(commit=False)
                        new_offer.app_id = curr_app
                        new_offer.save()
        elif rej_app := request.POST.get('reject'):
            rej_app.status = 'REJT'
            rej_app.save()
                
    return render(request, 'TinDevApp/recruiter_view_applicant.html', {'post': post, 'list': applicants, 'form':form, 'name':name, 'id_num':id_num })

def CandidateReject(request, name, id_num, app_id):
    app =  Application.objects.get(id=app_id)
    app.status = 'REJT'
    app.save()
    return render(request, 'TinDevApp/candidate_reject.html', {'name':name, 'id_num':id_num})

# View Posts of Candidate #

# View All Posts (including Active, Inactive, Not Interested)
def PostViewCandidateAll(request, name):
    application_list = list(Application.objects.filter(candidate_username=name).values_list('job_num',flat=True))
    post_list = list(Post.objects.all())
    applied_list = [x for x in post_list if x.id in application_list]
    return render(request, 'TinDevApp/candidate_view_post.html', {'post_list':post_list, 'apply_list': applied_list, 'name':name, 'active':'All'})

# View Active Posts
def PostViewCandidateActive(request, name):
    # if candidate is not interested in the post, hide it
    hide_list = NotInterest.objects.filter(candidate_username=name).values_list('job_num', flat=True)
    application_list = Application.objects.filter(candidate_username=name).values_list('job_num',flat=True)
    post_list = list(Post.objects.filter(active='A'))
    applied_list = [x for x in post_list if x.id in application_list]
    post_list = [x for x in post_list if (x.id not in hide_list and x.id not in application_list)]
    return render(request, 'TinDevApp/candidate_view_active_post.html', {'post_list':post_list, 'apply_list': applied_list, 'name':name, 'active':'Active'})

# View Inactive Posts
def PostViewCandidateInactive(request, name):
    # Candidate is still able to remove application
    application_list = Application.objects.filter(candidate_username=name).values_list('job_num',flat=True)
    post_list = list(Post.objects.filter(active='I'))
    applied_list = [x for x in post_list if x.id in application_list]
    #post_list = [x for x in post_list if x not in applied_list]
    return render(request, 'TinDevApp/candidate_view_inactive_post.html', {'post_list':post_list, 'apply_list': applied_list, 'name':name, 'active':'Inactive'})

# Search posts by description
def PostViewCandidateSearchDescription(request, name):
    application_list = Application.objects.filter(candidate_username=name).values_list('job_num',flat=True)
    post_list = list(Post.objects.all())

    query = request.GET.get("q")
    post_list = Post.objects.filter(
        Q(description__icontains=query) 
    )

    applied_list = [x for x in post_list if x.id in application_list]
    #post_list = [x for x in post_list if x not in applied_list]
    return render(request, 'TinDevApp/candidate_view_post.html', {'post_list':post_list, 'apply_list': applied_list, 'name':name, 'active':'Description Searched'})

# Search posts by zipcode
def PostViewCandidateSearchZipCode(request, name):
    application_list = Application.objects.filter(candidate_username=name).values_list('job_num',flat=True)
    post_list = list(Post.objects.all())

    query = request.GET.get("q")
    post_list = Post.objects.filter(
        Q(location__icontains=query) 
    )

    applied_list = [x for x in post_list if x.id in application_list]
    #post_list = [x for x in post_list if x not in applied_list]
    return render(request, 'TinDevApp/candidate_view_post.html', {'post_list':post_list, 'apply_list': applied_list, 'name':name, 'active':'Zipcode Searched'})


# Applications #

#Application Add/Delete #
def CandidateApply(request, name, id_num):
    apply = Application.objects.filter(candidate_username=name, job_num=id_num)
    if (len(apply) == 0):
        candidate = Candidate.objects.get(username=name)
        post = Post.objects.get(id=id_num)
        post.applicant_count += 1
        post.save()
        application = Application(job_num=id_num, job = post, candidate_username=name, 
                            candidate = candidate, status='APLY')
        application.save()

    return render(request, 'TinDevApp/candidate_apply_post.html', {'name':name})

# Remove Application
def CandidateRemoveApplication(request, name, id_num):
    apply = Application.objects.get(candidate_username=name, job_num=id_num)
    for offer in Offer.objects.filter(app_id=apply.id):
        offer.delete()
    apply.delete()
    post = Post.objects.get(id=id_num)
    post.applicant_count -= 1
    post.save()
    return render(request, 'TinDevApp/candidate_remove_apply.html', {'name':name})

#Application View
def CandidateViewApplication(request, name):
    apply = Application.objects.filter(candidate_username=name)

    return render(request, 'TinDevApp/candidate_view_applications.html', {'list':apply, 'name':name})

def CandidateViewOffer(request, name):
    apply = Application.objects.filter(candidate_username=name)

    return render(request, 'TinDevApp/candidate_view_offer.html', {'list':apply, 'name':name})

# Not interested in the Post
# Hide Post
def CandidateHideActivePost(request, name, id_num):
    dislike = NotInterest.objects.filter(candidate_username=name, job_num=id_num)
    post = Post.objects.get(id=id_num)
    if post.active == 'A':
        hide = NotInterest(job_num=id_num, candidate_username=name)
        hide.save()

    return redirect(reverse('TinDevApp:CandidateViewActive',kwargs={'name': name}))
    






