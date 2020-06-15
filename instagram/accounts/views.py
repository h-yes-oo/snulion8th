from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import get_object_or_404
from .models import Profile, Follow


def signup(request):
    if request.method == 'POST':
        if request.POST['id'] == '' or request.POST['password'] == '':
            return render(request, 'accounts/signup.html')
        elif request.POST['password'] == request.POST['password_check']:
            user = User.objects.create_user(username=request.POST['id'], password=request.POST['password'])
            user.profile.username = request.POST['username']
            auth.login(request, user)
            return redirect('/feeds/')
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request, username = request.POST['id'], password = request.POST['password'])
        if user:
            auth.login(request, user)
            return redirect('/feeds/')
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')
    

def follow_manager(request, pk):
    follow_from = Profile.objects.get(user_id = request.user.id)
    follow_to = Profile.objects.get(user_id = pk)

    try:
        following_already = Follow.objects.get(follow_to = follow_to, follow_from = follow_from)
    except Follow.DoesNotExist:
        following_already = None

    if following_already:
        following_already.delete()
    else:
        Follow.objects.create(follow_to = follow_to, follow_from = follow_from)
        
    return redirect('/feeds/')

