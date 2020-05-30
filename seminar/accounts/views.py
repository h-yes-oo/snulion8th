from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile, Follow
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


def follow_manager(request, pk):
    follow_from = Profile.objects.get(user_id=request.user.id)
    follow_to = Profile.objects.get(user_id=pk)

    try:
        following_already = Follow.objects.get(
            follow_from=follow_from, follow_to=follow_to)
    except Follow.DoesNotExist:
        following_already = None

    if following_already:
        following_already.delete()
    else:
        Follow.objects.create(follow_from=follow_from, follow_to=follow_to)
        # f = Follow()
        # f.follow_from, f.follow_to = follow_from, follow_to
        # f.save()

    return redirect('/feeds')

    # def login(request):
    #     if request.method == 'POST':
    #         user = auth.authenticate(
    #             request, username=request.POST['username'], password=request.POST['password'])
    #         if user is not None:
    #             return redirect('/feeds')

    #     return render(request, 'accounts/login.html')
    # def logout(request):
    #     return render(request, 'accounts/logout.html')
