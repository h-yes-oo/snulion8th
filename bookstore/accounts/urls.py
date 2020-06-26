from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]