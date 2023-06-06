from django.contrib import admin
from django.urls import path

from VSgames import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('created_post/', views.PostCreate.as_view()),
    path('<int:pk>/add_comment/', views.add_comment),
    path('<int:pk>/voting/', views.VoteDetail.as_view()),
    path('<int:pk>/voting/add_vote/', views.add_vote),
]
