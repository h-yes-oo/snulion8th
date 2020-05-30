from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create,name='create'),
    path('<int:id>/', views.read, name='read'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/',views.edit, name='edit'), 
]