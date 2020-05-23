from django.conf.urls import include
from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # 작동하지 않는 url이었다... 이유는 url include를 해주지 않았기 때문. 
    # path('signup/', views.signup, name='signup'),
    # path('profile_edit/<int:id>/', views.profile_edit, name="profile_edit"),
]