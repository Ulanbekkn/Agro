from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.product.views import *

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'add_images', ProductImageViewSet, basename='add_images')

urlpatterns = [
    path('', include(router.urls)),
]


