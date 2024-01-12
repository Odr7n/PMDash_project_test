"""
URL configuration for NewsStudyRTK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('main/', views.mainBoard, name='pmdash_main'),
    path('all/', views.allBoards, name='pmdash_all'),
    path('account/', views.account, name='pmdash_account'),
    path('contacts/', views.contacts, name='pmdash_contacts'),
    path('', views.index, name='pmdash_home'),
    path('dashboards/<int:id>/', views.detail, name='pmdash_detail')
]
