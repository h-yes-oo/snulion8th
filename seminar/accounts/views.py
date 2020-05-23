from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .models import Profile, Follow

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            profile = user.profile
            profile.college = request.POST['college']
            profile.major = request.POST['major']
            profile.birthday = request.POST['birthday']
            profile.sns = request.POST['sns']
            user.save()
            auth.login(request, user)
            return redirect('/feeds/')
    return render(request, 'accounts/signup.html')

def myinfoedit(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile
        profile.college = request.POST['college']
        profile.major = request.POST['major']
        profile.birthday = request.POST['birthday']
        profile.sns = request.POST['sns']
        user.save()
        return redirect('/feeds')
    return render(request, 'accounts/myinfoedit.html')

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
        f = Follow()
        f.follow_from, f.follow_to = follow_from, follow_to
        f.save()
    
    return redirect('/feeds')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/feeds/')
#         else:
#             return render(request, 'accounts/login.html')
#     else:
#         return render(request, 'accounts/login.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('/feeds/')