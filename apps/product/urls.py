from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.product.views import ProductViewSet, CommentCreateView

router = SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('comment/', CommentCreateView.as_view())
]

urlpatterns += router.urls
    