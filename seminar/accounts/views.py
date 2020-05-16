from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'])
            Profile.objects.filter(user_id=user.id).update(
                college=request.POST['college'],
                major=request.POST['major'],
                birth=request.POST['birth'],
                sns=request.POST['sns'])
            user.refresh_from_db()
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html')


"""
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('feeds')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')
"""
