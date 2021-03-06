"""prodHealthApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# CSS
# https://docs.djangoproject.com/en/3.1/howto/static-files/
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
#journaling pages
from journaling.views import (
        journaling_create_view,
        journaling_list_view
    )
#general pages
from pages.views import (
        home_view,
        about_view,
        contact_view
    ) 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    # will have to make the address better(inside the app folder)
    path('journalList/', journaling_list_view),
    path('journalCreate/',  journaling_create_view)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
