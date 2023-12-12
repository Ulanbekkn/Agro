from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.product.views import *

router = DefaultRouter()
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_product/', UserPostsListView.as_view(), name='user_product'),  

]
