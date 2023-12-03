from rest_framework import generics
from apps.product.models import Product, Comment
from apps.product.serializers import ProductListSerializer, CommentSerializer, ProductDetailSerializer
from apps.product.permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductDetailSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
