"""
URL configuration for MP13Bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

import debug_toolbar
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse
from MP13Bookstore import views

def home(request):
    return HttpResponse("🚀 A API está no ar! Veja /bookstore/v1/product/ ou /bookstore/v1/order/")

def update_server(request):
    return HttpResponse("Servidor atualizado com sucesso!")

urlpatterns = [
    path("", home),
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path('hello/', views.hello_world, name='hello_world'),
    path('update_server/', views.update, name='update_server'),
]
