from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, SkillProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "username", "email", "mobile", "user_type"
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "mobile", "user_type", "password", "confirm_password"]

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")  # remove confirm_password
        
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            mobile=validated_data.get("mobile"),
            user_type=validated_data.get("user_type", "student"),
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        data["user"] = user
        return data
