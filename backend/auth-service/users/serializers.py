from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid username or password")

        refresh = CustomTokenObtainPairSerializer.get_token(user)

        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email',''),
            first_name=validated_data.get('first_name',''),
            last_name=validated_data.get('last_name',''),
            password=validated_data['password']
        )

        return user



class UpdateUserSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=False)
    new_password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=False)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'old_password', 'new_password', 'confirm_password')

        def validate(self,data):
            if data.get('new_password') and data.get('confirm_password'):
                if data['new_password'] != data['confirm_password']:
                    raise serializers.ValidationError("Passwords don't match")

            if data.get('new_password') and not data.get('old_password'):
                raise serializers.ValidationError("Old password can't be blank")

            return data

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            new_password = validated_data.get('new_password')
            old_password = validated_data.get('old_password')

            if new_password and old_password:
                if not instance.check_password(old_password):
                    raise serializers.ValidationError("Old password can't be blank.")
                instance.set_password(new_password)

            instance.save()
            return instance
