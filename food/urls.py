"""aichi URL Configuration

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
from django.urls import path
from . import views
from food.views import StoreListView, StoreDetailView, formfunc

# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


app_name = "stores"

urlpatterns = [
    path('index', views.index, name='index'),
    path('post', formfunc, name='post'),
    path('post_fin', views.fin, name='post_fin'),
    path('post_delete', views.delete, name='post_delete'),
    path('other', views.other, name='other'),
    path('research', StoreListView.as_view(), name='research'),
    path('<int:pk>/', StoreDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),


    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
]


