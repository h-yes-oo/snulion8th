from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth # base.html에서 user.is_authenticated, user.get_username 등을 사용할 수 있음
from django.shortcuts import redirect

# Create your views here.
def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/feeds')
    return render(request, 'accounts/signup.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username = username, password = password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/feeds')
#         else:
#             return render(request, 'accounts/login.html', {'error' : 'username or password is incorrect'})
#     else:
#         return render(request, 'accounts/login.html')

# def logout(request):
#     # user = User.objects.get(id=id)
#     auth.logout(request)
    # return render(request, 'accounts/logout.html')
    # return redirect('/feeds')
