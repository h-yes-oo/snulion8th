from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.
def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.profile.college = request.POST['college']
            user.profile.major = request.POST['major']
            # Profile.objects.all()
            # Profile.objects.update(user=user, college=request.POST['college'], major=request.POST['major'])
            # Profile.objects.update(user=user, college=request.POST['college'], major= request.POST['major'])
            auth.login(request, user)
        return redirect('/feeds')
    return render(request, 'accounts/signup.html')


def logout(request):
    return render(request, 'accounts/logout.html')

# def login(request):
#     if request.method  == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username = username, password = password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect ('/feeds')
#         # else:
#         #     return render(request)

#         elif: return "등록되지 않은 id입니다"
#     'username'
#     'password'

#     return render(request, 'accounts/login.html')