from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as custom_logout
from .models import Profile, Follow


def signup(request):
    if request.method == 'POST':
        if (request.POST['password1'] == request.POST['password2']) & (request.POST['seed'] == '0'):
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])##여기다가 확장한 variable들 쓰면 왜 안되는지? 확장한게 아닌 원래 user에 있는 variable만 접근가능해서?
            profile = user.profile
            profile.college=request.POST['college']
            profile.major=request.POST['major']
            profile.birthdate=request.POST['birthdate']
            profile.contact=request.POST['contact']
            user.save()
            auth.login(request, user)
            return redirect('/feeds/')
        elif request.POST['seed'] != '0':
            # a=Profile()
            Profile.seed(int(request.POST['seed']))
            return redirect('/feeds/')

    return render(request, 'accounts/signup.html')


def myedit(request):
    if request.method == 'POST':
        user = request.user
        # user = User.objects.get(username=request.POST['username'])
        profile = user.profile
        profile.college=request.POST['college']
        profile.major=request.POST['major']
        profile.birthdate=request.POST['birthdate']
        profile.contact=request.POST['contact']
        user.save()
        return redirect('/feeds')
    return render(request, 'accounts/myedit.html')


def follow_manager(request, pk):
    follow_from = Profile.objects.get(user_id = request.user.id)
    follow_to = Profile.objects.get(user_id = pk)

    try:
        following_already = Follow.objects.get(follow_from=follow_from, follow_to=follow_to)
    except Follow.DoesNotExist:
        following_already = None

    if following_already:
        following_already.delete()
    else:
        # Follow.objects.create(follow_from=follow_from, follow_to=follow_to)
        f = Follow()
        f.follow_from, f.follow_to = follow_from, follow_to
        f.save()

    return redirect('/feeds')