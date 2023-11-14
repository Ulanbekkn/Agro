from rest_framework import generics
from rest_framework.response import Response
from .models import ProfileUser
from .serializers import ProfileUserSerializer
from rest_framework.permissions import IsAuthenticated
 
class ProfileUserAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        profile = self.get_object()
        serializer = ProfileUserSerializer(instance=profile)
        return Response(serializer.data)
    
    def patch(self, request):
        profile = self.get_object()
        serializer = ProfileUserSerializer(instance=profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get_object(self):
        return ProfileUser.objects.get(user=self.request.user)
