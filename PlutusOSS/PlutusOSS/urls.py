from django.conf.urls import url, include
import rest_framework
from django.urls import path
from rest_framework import routers
from data import views
from rest_framework.authtoken import views as tokenviews
from django.contrib import admin

"""PlutusOSS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

router = routers.DefaultRouter()
router.register(r'stock', views.StockViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-token-auth/', tokenviews.obtain_auth_token), #returns token for account, when correct login
    url(r'^api-auth/', include('rest_framework.urls')), #Login button
]

