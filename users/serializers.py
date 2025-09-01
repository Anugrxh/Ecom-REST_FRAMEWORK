from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ("fullname", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            fullname=validated_data['fullname'],
            password=validated_data['password'],
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "fullname", "email", "profile_image", "phone_number", "address_line", "pincode", "nearest_area")
        read_only_fields = ("email",)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("fullname", "profile_image", "phone_number", "address_line", "pincode", "nearest_area")
