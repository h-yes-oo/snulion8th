from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.shortcuts import redirect

# Create your views here.
def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],\
                                            password=request.POST['password1'])
            auth.login(request, user)
            Profile.objects.filter(user = user).update(college = request.POST['college'],\
                                major = request.POST['major'], sns = request.POST['sns'],\
                                birthday = request.POST['birthday'])
            return redirect('/feeds')
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/feeds')
        else:
            return render(request, 'accounts/login.html')
            # , 'error':'username or password is incorrect')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logged_out.html')

def user_edit(request, id):
    if request.method == 'POST':
        user = User.objects.get(id = id)
        Profile.objects.filter(user = user).update(college = request.POST['college'],\
                                major = request.POST['major'], sns = request.POST['sns'],\
                                birthday = request.POST['birthday'])
        return redirect('/feeds')

    elif request.method == 'GET':
        return render(request, 'accounts/user_edit.html')


