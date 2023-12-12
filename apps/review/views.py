from rest_framework import generics
from .serializers import FavoriteListSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return self.request.user.favorites.all()
    