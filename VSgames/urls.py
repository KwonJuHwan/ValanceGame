from django.contrib import admin
from django.urls import path

from VSgames import views

app_name = "Post"

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('hot/created_post/', views.PostCreate.as_view()),
    path('created_post/', views.PostCreate.as_view()),
    path('<int:pk>/add_comment/', views.add_comment),
    path('<int:pk>/voting/', views.VoteDetail.as_view()),
    path('<int:pk>/voting/add_vote/', views.add_vote),
    path('<int:pk>/user/', views.UserDetail.as_view()),
    path('<int:pk>/user/user_post/', views.post_page),
    path('hot/', views.hot_page),
    path('<int:pk>/delete_post', views.delete_post)

]
