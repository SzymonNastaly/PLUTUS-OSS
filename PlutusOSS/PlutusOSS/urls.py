from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from data import views
from rest_framework.authtoken import views as tokenviews
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'stock', views.StockViewSet)

urlpatterns = [
    path('api/', include(router.urls), name="api"),
    path('admin/', admin.site.urls),
    path('api-token-auth/', tokenviews.obtain_auth_token), #returns token for account, when correct login
    path('api-auth/', include('rest_framework.urls')), #Login button
    path('signup/', views.signup),
    path('', views.index),
]

