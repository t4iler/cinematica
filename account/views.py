from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


from cinematica.tasks import send_email_task     # вместо send_confirmation_email
from .send_email import send_reset_password, send_html_email
from . import serializers


User = get_user_model()

class RegistrationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                # send_confirmation_email(user)
                send_email_task.delay(user.email, user.activation_code) # паралельная отправка и дальнейшее действие без ожидания
            return Response(serializer.data, status=201)
        return Response(status=400)



class ActivationView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'Message': 'Successfully activated!'}, status=200)
        except User.DoesNotExist:
             return Response({'Message': 'Link expired!'}, status=400)
             
# =============================================================================================

class LoginApiView(TokenObtainPairView):
    serializer_class = serializers.LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "success",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )

class LogoutApiView(GenericAPIView):
    serializer_class = serializers.LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully logged out!', status=204)
    

class ForgotPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(email=serializer.data.get('email'))
            user.create_activation_code()
            user.save()
            send_reset_password(user)
            return Response('Check your mail!', status=200)
        except User.DoesNotExist:
            return Response('User with this email does not exist!', status=400)

class RestorePasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.RestorePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Password changed successfully!', status=200)
    

class FollowSpamApi(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.FollowSpamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            send_html_email()
            return Response('Followed to spam!', status=200)


