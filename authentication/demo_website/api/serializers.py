from rest_framework import serializers
from .models import *



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginInfo
        fields = ['login', 'password']
 