from django.conf.urls import include
from django.urls import path
from feedpage import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
]