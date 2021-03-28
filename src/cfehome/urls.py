"""cfehome URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from products.views import ProductListView, ProductDetailView, DigitalProductListView, ProductRedirectView, ProductIDRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('digital/', DigitalProductListView.as_view()),
    path('products/', ProductListView.as_view()),
    # path('products/<int:id>/', ProductDetailView.as_view()),
    path('a/<slug:slug>/', ProductRedirectView.as_view()),
    path('b/<slug:slug>/', ProductRedirectView.as_view()),
    path('p/<int:pk>/', ProductIDRedirectView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view()),
]
