from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('<int:id>/', views.show, name='show'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
    
=======
=======
>>>>>>> parent of f3173ac... 2-CRUD-homework
    path('<int:id>', views.show, name='show'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/editApply', views.editApply, name='editApply'),
<<<<<<< HEAD
>>>>>>> parent of f3173ac... 2-CRUD-homework
=======
>>>>>>> parent of f3173ac... 2-CRUD-homework
]