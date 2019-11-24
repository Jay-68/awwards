# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration.html', {'form': form})


@login_required(login_url='/accounts/login/')
def index(request):

    message = "Hello World"

    profiles = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()

    context = {"profiles": profiles, "projects": projects,
               "reviews": reviews, "message": message}

    return render(request, 'index.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)

    users = User.objects.get(username=username)
    id = request.user.id
    form = ProfileForm()

    try:
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)

    projects = Project.get_profile_pic(profile.id)
    return render(request, 'registration/profile.html', {'title': title, 'profile': profile, "projects": projects, 'profile_info': profile_info, "form": form})
