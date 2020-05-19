from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .models import Profile

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