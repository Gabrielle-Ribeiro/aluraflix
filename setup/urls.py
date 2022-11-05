from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from api.views import VideoViewSet


router = routers.DefaultRouter()
router.register('videos', VideoViewSet, basename='Videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
