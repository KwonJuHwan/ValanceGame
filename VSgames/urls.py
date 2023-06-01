
from django.contrib import admin
from django.urls import path

from VSgames import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]