from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, Follow
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