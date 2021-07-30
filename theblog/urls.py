from os import name
from .views import HomeView,ArticleDetailView,UpdatePostView,DeletePostView
from django.urls import path
from theblog.views import *
urlpatterns = [
    # path('', views.home,name="home")
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name="article-detail"),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('article/update/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name="delete_post"),
]
