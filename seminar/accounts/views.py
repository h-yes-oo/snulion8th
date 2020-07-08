from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile, Follow
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import JsonResponse

def signup(request):
   if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password1"]
        college = request.POST["college"]
        major = request.POST["major"]

        user = User.objects.create_user(username=username, email=email, password=password)
        user.profile.college = college
        user.profile.major = major
        user.save()

        login_user = django_authenticate(username=username, password=password)
        django_login(request, login_user)
        return JsonResponse({"response": "signup success"})
       

    

def mypage(request):
    if request.method == 'POST':
        user=request.user
        user.name=request.POST['username']
        user.profile.college = request.POST['college']
        user.profile.major = request.POST['major']
        auth.login(request, user)
        return redirect('/feeds')
    else:
        return render(request, 'accounts/mypage.html')


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