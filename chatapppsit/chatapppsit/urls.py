"""chatapppsit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#เอาไว้เก็บการroutingของhttp request และกำหนด url pattern
from django.contrib import admin
from django.urls import path
from Chatapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginform),
    path('signup', views.signup),
    path('register', views.register),
    path('login', views.login),
    path('home', views.home),
    path('logout', views.logout),
    path('profile', views.profile),
    path('<str:room>/', views.chatroom, name='room'),
    path('checkroom', views.checkroom, name='checkroom'),
    path('send', views.send, name='send'),
    path('getallMessages/<str:room>/', views.allmessage)
    
]
