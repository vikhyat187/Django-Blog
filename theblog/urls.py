from os import name
from .views import HomeView,ArticleDetailView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView,AddCommentView
from django.urls import path,include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from theblog.views import *
urlpatterns = [
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    # path('', views.home,name="home")
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name="article-detail"),
    path('add_post/',AddPostView.as_view(),name="add_post"),
    path('article/<int:pk>/comment/',AddCommentView.as_view(),name="add_comment"),
    path('add_category/',AddCategoryView.as_view(),name="add_category"),
    path('article/update/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name="delete_post"),
    path('category/<str:cats>/',CategoryView,name="category"),
    path('category-list/',CategoryListView,name="category-list"),
    path('like/<int:pk>',LikeView,name="like-post"),
]
