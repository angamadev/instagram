"""
URL configuration for conquerblocks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import (
    ProfileListView,
    ProfileDetailView,
    ProfileUpdateView,
    # BlogCreateView,
    # BlogDeteteView,
)
app_name = "profiles"

urlpatterns = [
    path("list",ProfileListView.as_view(), name="profile_list"),
    path("<pk>", ProfileDetailView.as_view(), name="profile_detail"),
    # path("nuevo/", BlogCreateView.as_view(), name="blog_create"),
    path("update/<pk>", ProfileUpdateView.as_view(), name="profile_update"),
    # path("borrar/<pk>", BlogDeteteView.as_view(), name="blog_delete"),
    
]
