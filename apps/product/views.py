from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from apps.product.models import *
from apps.product.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.review.serializers import FavoriteCreateSerializer
from apps.review.models import Favorite
from apps.product.permissions import IsAuthor



class PermissionMixin:
    def get_permissions(self):
        if self.action in ('create',):
            permissions = [IsAuthenticated,]
        elif self.action in ('update','partial_update','destroy',):
            permissions = [IsAuthor,]
        else:
            permissions = [AllowAny,]
        return [permission() for permission in permissions]


class ProductViewSet(PermissionMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        product = self.get_object()
        user = request.user
        serializer = FavoriteCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                fav_post = Favorite.objects.get(product=product, author=user)
                fav_post.delete()
                message = 'deleted from favorites'
            except Favorite.DoesNotExist:
                Favorite.objects.create(product=product, author=self.request.user)
                message = 'added to favorites'
            return Response(message, status=201)
    
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    


class UserPostsListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    



# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     permission_classes = (IsOwnerOrReadOnly,)

    # def get_serializer_class(self):
#         if self.action == 'list':
#             return ProductListSerializer
#         else:
#             return ProductDetailSerializer


# class CommentCreateView(generics.CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



