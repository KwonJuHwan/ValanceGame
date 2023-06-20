from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('vs/', include('VSgames.urls')),
    path('',include('main_page.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
