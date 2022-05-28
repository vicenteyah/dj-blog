from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    BlogViewSet,
)
router = DefaultRouter()
router.register(r'posts', BlogViewSet, basename='posts')

app_name='blog'

urlpatterns = [
    path('api/', include(router.urls)),
]
