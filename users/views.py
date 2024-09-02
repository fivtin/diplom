
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import (
    JWTTokenObtainPairSerializer,
    UserCreateSerializer)


class JWTTokenObtainPairView(TokenObtainPairView):
    serializer_class = JWTTokenObtainPairSerializer


class UserCreateAPIView(CreateAPIView):
    """Create user."""

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
