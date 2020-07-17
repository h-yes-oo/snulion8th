from django.urls import path
from feedpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>/show/', views.show, name='show'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/comment/', views.feed_comment, name='comment'),
    path('<int:id>/comment/<int:cid>/delete', views.comment_delete, name="comment_delete"),
    path('<int:pk>/like/', views.feed_like, name='like'),
]
