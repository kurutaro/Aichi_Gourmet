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
from food.views import ReviewListView

urlpatterns = [
    path('index.html', views.index, name='index'),
    # path('about.html', views.about, name='about'),
    path('products.html', views.products, name='products'),
    path('store.html', views.store, name='store'),

    path('about.html', ReviewListView.as_view(), name='research'),
]
