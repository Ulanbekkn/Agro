from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView



urlpatterns = [
    path('reg/', CreateAccountView.as_view()),
    path('act/<str:email>/<str:activation_code>', ActivationView.as_view(), name='activation'),
    path('log/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('ref/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('ch-pass/', ChangePasswordView.as_view()),
    path('for-pass/', ForgotPasswordView.as_view()),
    path('for-pass-compl/', ForgotPasswordCompleteView.as_view()),
]