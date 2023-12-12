from rest_framework.viewsets import ModelViewSet, GenericViewSet
# from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from apps.product.models import *
from apps.product.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.review.models import Favorite
from apps.review.serializers import FavoriteCreateSerializer
# from apps.product.permissions import IsAuthor



# class PermissionMixin:
    # def get_permissions(self):
    #     if self.action in ('create',):
    #         permissions = [IsAuthenticated,]
    #     elif self.action in ('update','partial_update','destroy',):
    #         permissions = [IsAuthor,]
    #     else:
    #         permissions = [AllowAny,]
    #     return [permission() for permission in permissions]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    # print(queryset)
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer


    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = FavoriteCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                fav_post = Favorite.objects.get(product=product, user=user)
                fav_post.delete()
                message = 'Удален из избранных'
            except Favorite.DoesNotExist:
                Favorite.objects.create(product=product, user=self.request.user)
                message = 'Добавлен в избранные'
            return Response(message, status=201)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    


class ProductImageViewSet(CreateModelMixin, 
                          DestroyModelMixin, 
                          GenericViewSet):
    
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]



# class CommentCreateView(generics.CreateAPIView):
    # queryset = Comment.objects.all()
    # serializer_class = CommentSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



