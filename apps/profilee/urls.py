from django.urls import path
from .views import ProfileUserAPIView

urlpatterns = [
    path('user/', ProfileUserAPIView.as_view()),
]