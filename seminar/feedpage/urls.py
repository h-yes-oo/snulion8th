from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.index, name='index'),
]
