from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.profile.college = request.POST['college']
            user.profile.major = request.POST['major']
            user.profile.email = request.POST['email']
            user.profile.post = request.POST['post']
            auth.login(request, user)
        return redirect('/feeds')
    return render(request, 'accounts/signup.html')

