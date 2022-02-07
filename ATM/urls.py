"""ATM_MACHINE URL Configuration

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
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('logincheck',views.logincheck,name="logincheck"),
    path('reg',views.reg,name="reg"),

    path('dashboard',views.dashboard,name="dashboard"),

    path('edit',views.edit,name="edit"),
    path('update',views.update,name="update"),
    path('debit',views.debit,name="debit"),
    path('deb',views.deb,name="deb"),
    path('withdraw',views.withdraw,name="withdraw"),
    path('logout',views.logout,name="logout"),
   
]
