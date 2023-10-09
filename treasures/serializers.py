from rest_framework import serializers
from treasures.models import CustomUser, Treasure
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):

    # Modify the default behavior to set encrypted passwords
    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, CustomUser):
        token = super(MyTokenObtainPairSerializer, cls).get_token(CustomUser)

        # Add custom claims
        token['username'] = CustomUser.username
        # token['password'] = user.password
        return token
    

class TreasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasure
        fields = ['id', 'name', 'price', 'description']