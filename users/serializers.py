from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer

from users.models import User


class JWTTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        del representation['password']
        return representation
