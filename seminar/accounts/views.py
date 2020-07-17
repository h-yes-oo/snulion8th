# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password
from .models import Profile, Follow
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import JsonResponse


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        college = request.POST["college"]
        major = request.POST["major"]
        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.profile.college = college
            user.profile.major = major
            user.save()

            login_user = django_authenticate(username=username, password=password1)
            django_login(request, login_user)

        return JsonResponse({"response": "signup success"})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/feeds')
        else:
            return render(request, 'accounts/login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')


    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logged_out.html')

def pwchange(request):
    if request.method  == 'POST':
        passwordbefore = request.POST['passwordbefore']
        passwordafter1 = request.POST['passwordafter1']
        passwordafter2 = request.POST['passwordafter2']
        user = request.user
        if check_password(passwordbefore, user.password) and passwordafter1 == passwordafter2:
            user.set_password(passwordafter1)
            user.save()
            return redirect('/feeds')
    return render(request, 'accounts/editaccount.html')


def editaccount(request):
    if request.method  == 'POST':
        passwordbefore = request.POST['passwordbefore']
        user = request.user
        if check_password(passwordbefore, user.password):
            Profile.objects.filter(user=user).update(college = request.POST['college'], major= request.POST['major'])
            return redirect('/feeds')
    return render(request, 'accounts/editaccount.html')

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
        Follow.objects.create(follow_from=follow_from, follow_to=follow_to)

    return redirect('/feeds')

