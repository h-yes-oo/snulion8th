from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.forms import UserChangeForm
#from accounts import CustomUserChangeForm

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            profile=user.profile
            profile.college=request.POST['college']
            profile.major=request.POST['major']
            profile.mbti=request.POST['mbti']
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html')

def login (request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request,user)
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')
    

def logout(request):
    return render(request, 'accounts/logout.html')

'''@login_required
def update(request):
    if request.method=='POST':
        user_change_from= CustomUserChangeForm(requst.POST,instance=request.user)
        user_change_form.save()
    else:
        user_change_from= CustomUserChangeForm(requst.POST,instance=request.user)
        return render(request, 'accounts/update.html', {'user_change_form':user_change_form})
'''