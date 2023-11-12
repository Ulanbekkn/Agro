from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import ChangePasswordSerializer, ForgotPasswordSerializer, ForgotPasswordCompleteSerializer
from rest_framework.permissions import IsAuthenticated



User = get_user_model()



class CreateAccountView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
        return Response('Вы успешно зарегистрировались', status=201)
    

        
class ActivationView(APIView):

    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('Пользователь не найден', status=400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Аккаунт успешно активирован', status=200)



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлен')



class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_email()
            return Response('Вам было отправлено сообщение для восстановления')



class ForgotPasswordCompleteView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно изменен')