from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile
from faker import Faker


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            user.profile.college = request.POST['college']
            user.profile.major = request.POST['major']
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html')


def profile_edit(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        Profile.objects.filter(user=user).update(
            college=request.POST['college'], major=request.POST['major'])
        return redirect('/feeds')

    return render(request, 'accounts/profile_edit.html')


# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(
#             request, username=request.POST['username'], password=request.POST['password'])
#         if user is not None:
#             return redirect('/feeds')

#     return render(request, 'accounts/login.html')


# def logout(request):
#     return render(request, 'accounts/logout.html')
