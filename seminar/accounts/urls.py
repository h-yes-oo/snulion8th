from django.conf.urls import include
from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('edit/', views.edit, name='mypage'),
    path('<int:pk>/follow/', views.follow_manager, name='follow'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]