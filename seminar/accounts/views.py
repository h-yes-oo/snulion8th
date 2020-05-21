from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile

# Create your views here.

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1']==request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            user.profile.college = request.POST['college']
            user.profile.major = request.POST['major']
            user.profile.birth = request.POST['birth']
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html',)


def profile(request):
    return redirect(request, 'accounts/profile.html',)


def profile_update(request, id):
    user.profile.college = request.POST['college']
    user.profile.major = request.POST['major']
    user.profile.birth = request.POST['birth']
    user.profile.save()
    return redirect('/feeds')


def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')
