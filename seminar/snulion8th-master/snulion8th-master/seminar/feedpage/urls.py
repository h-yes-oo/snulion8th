from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/',views.new,name='new'),
    path('<int:id>', views.show, name='show'),
    path('<int:id>/edit',views.edit, name='edit'),
    path('<int:id>/delete',views.delete,name='delete'),
    path('<int:id>/comments/',views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>/',views.delete_comment,name='delete_comment'),
    path('<int:pk>/like/',views.feed_like, name='like'),
    path('map/',views.map, name='map'),
]