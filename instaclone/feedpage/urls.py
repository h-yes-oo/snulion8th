from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create,name='create'),
    path('<int:id>/', views.read, name='read'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/',views.edit, name='edit'), 
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>',views.delete_comment, name='delete_comment'),
]