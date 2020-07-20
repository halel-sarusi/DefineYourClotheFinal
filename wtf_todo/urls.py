"""wtf_todo URL Configuration

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
from django.urls import path
from todo import views
from todo import models
from django.utils import timezone


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerForm, name='registerForm'),
    path('myitems/', views.myitems,name='myitems'),
    path('', views.homepage, name='homepage'),
    path('logout', views.logoutuser, name ='logoutuser'),
    path('login/', views.loginuser, name ='loginuser'),
    path('newitem/', views.newitem, name='newitem'),  
    path('mainpage/', views.mainpage, name='mainpage'),
    path('baskets/', views.baskets, name='baskets'),
    path('darksoft/', views.darksoft, name='darksoft'),
    path('myitems/todo/<int:todo_pk>', views.edititem, name='edititem'),
    path('todo/<int:todo_pk>/done', views.donetodo, name='donetodo'),
    path('todo/<int:todo_pk>/delete', views.deleteTodo, name='deleteTodo'),
    path('allitems/', views.allitems, name='allitems'),
    path('assigntome/<int:todo_pk>', views.assigntome, name='assigntome'),
]
