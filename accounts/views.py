from rest_framework.permissions import AllowAny
from accounts.serializers import (
    RegistrationSerializer,
    UserSerializer,
    LoginSerializer
    )
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from core.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class RegisterAPI(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, tokens = serializer.save()

        # Serialize the user to get a JSON-serializable representation
        user_data = serializer.to_representation(user)
        response_data = {
            'user': user_data,
            'tokens': tokens
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginAPI(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            serialized_user = UserSerializer(user).data
            refresh = RefreshToken.for_user(user)

            response = {
                'user': serialized_user,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }

            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserApi(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserApi(APIView):
    # queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        user = User.objects.filter(is_superuser=False)

        return Response(user)

    def post(self, request, format=None):
        return Response("ASDASD")
