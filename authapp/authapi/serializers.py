from rest_framework import serializers
from .models import SignUpModel, LogInModel

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpModel
        fields = ["username", "email", "password"]

class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogInModel
        fields = ["username", "password"]