from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from apps.product.models import *
from apps.product.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.review.models import Favorite, Comment
from apps.review.serializers import FavoriteCreateSerializer, CommentSerializer
from rest_framework import generics






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
    

    @action(methods=['POST', 'PATCH','DELETE'], detail=True, permission_classes=[IsAuthenticated])
    def comment(self, request, pk=None):
        product = self.get_object()
        user = request.user
        try:
            comment = Comment.objects.get(product=product,user=user)
        except Comment.DoesNotExist:
            comment = None
        if request.method == 'POST':
            serializer = CommentSerializer(data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save(product=product, user=user)
                return Response('Комментарий создан', status=201)
        elif request.method == 'PATCH':
            if not comment:
                return Response('Вы еще не оставляли комментарий для этого поста', status=400)
            serializer = CommentSerializer(instance=comment,data=request.data, context={'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response('Комментарий успешно обновлен', status=200)
        elif request.method == 'DELETE':
            if not comment:
                return Response('Вы еще не оставляли комментарий для этого поста', status=400)
            comment.delete()
            return Response('Комментарий успешно удален', status=204)




class ProductImageViewSet(CreateModelMixin, 
                          DestroyModelMixin, 
                          GenericViewSet):
    
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]


class CategoryView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    
    def get_queryset(self):
        category_slug = self.kwargs['category']
        category = category_slug.replace('-', ' ')
        queryset = Product.objects.filter(category=category)
        print(category_slug)
        print(category)
        print(queryset)
        return queryset
        