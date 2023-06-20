from django.urls import path

from main_page import views

urlpatterns = [
    path('', views.main),

]
