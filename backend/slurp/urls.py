from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from . import views


api_router = routers.DefaultRouter()
api_router.register(r'consumptions', views.ConsumptionViewSet)
api_router.register(r'people', views.PersonViewSet)

urlpatterns = [
    url(r'^api/', include(api_router.urls)),
    url(r'^admin/', admin.site.urls),
]
