"""Proyectos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from users import views #usuarios



urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',include('holamundo.urls'))
    #path('',include('blog.urls'))
    #url(r'^',include('blog.urls')),
    url(r'^admin/',admin.site.urls),#incrmento django admin
    url(r'^$',views.welcome, name = 'welcome'),#iuncremento seccion usuarios
    path(r'^',include('fempleados.urls')),#incremento
    path(r'^',include('blog.urls')),#incremento
    

    #seccion usuarios
    path('',views.welcome),
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #incremento
