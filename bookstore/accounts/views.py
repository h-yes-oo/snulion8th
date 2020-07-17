from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user_id = request.POST['user_id']
            password = request.POST['password1']
            user = User.objects.create_user(username = user_id, password = password)
            user.profile.phone = request.POST['phone_number']
            user.profile.name = request.POST['user_name']
            auth.login(request, user)
            return redirect('/store/')
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request, username = request.POST['user_id'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/store/')
    return render(request, 'accounts/login.html')
        