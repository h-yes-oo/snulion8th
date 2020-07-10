from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile, Follow
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import JsonResponse

# Create your views here.

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



def user_info(request, id):
    if request.method == 'POST':
        user=User.objects.get(id=id)
        user.username = request.POST['new_username'] #???? 유저네임 이메일 같은 것도 바꾸는거 가능한가요
        user.email    = request.POST['new_email']
        # user.set_password(request.POST['new_password']) 
        user.save()
        Profile.objects.filter(user=user).update(college  = request.POST['new_college'],\
                                                 major    = request.POST['new_major'],\
                                                 birthday = request.POST['new_birthday'])
        return redirect('/feeds')
    else:
        return render(request, 'accounts/user_info.html')
    
def follow_manager (request, pk):
    follow_from = Profile.objects.get(user_id = request.user.id)
    follow_to = Profile.objects.get(user_id = pk)

    try:
        following_already = Follow.objects.get(follow_from=follow_from, follow_to=follow_to)
    except Follow.DoesNotExist:
        following_already=None
    
    if following_already:
        following_already.delete()
    else:
        f=Follow()
        f.follow_from, f.follow_to = follow_from, follow_to
        f.save()
    
    return redirect('/feeds')