from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html')


# def login(request):
#     if request.method  == 'POST':

#         username_input = request.POST['username']
#         password_input = request.POST['password']

#         user = auth.authenticate(request, username = username_input, password = password_input)

#         if user is not None:
            
#             auth.login(request, user)
#             return redirect('/feeds')
        

#     return render(request, 'accounts/login.html')

# def logout(request):
#     return render(request, 'accounts/logout.html')