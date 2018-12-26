from django.conf.urls import url, include
import rest_framework
from django.urls import path
from rest_framework import routers
from data import views
from rest_framework.authtoken import views as tokenviews
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'stock', views.StockViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls), name="api"),
    path('admin/', admin.site.urls),
    url(r'^api-token-auth/', tokenviews.obtain_auth_token), #returns token for account, when correct login
    url(r'^api-auth/', include('rest_framework.urls')), #Login button
    url(r'^signup/', views.signup),
    url(r'^', views.index),
]

