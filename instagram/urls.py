"""
URL configuration for instagram project.

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
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from .views import (
    HomeView,
    logout_view,
    MyLoginView,
    ContactUsFormView,
    # CustomLogoutView,
    RegisterView,
)

from django.conf import settings

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path("",HomeView.as_view(), name="home"),
    path("login",MyLoginView.as_view(), name="login"),
    path("registro", RegisterView.as_view(), name='registro'),
    path("logout",logout_view, name="logout"),
    path("contact", ContactUsFormView.as_view(), name='contacto'),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls')),
    ]
