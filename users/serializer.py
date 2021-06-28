from django.db import models
from rest_framework.serializers import ModelSerializer
from users.models import UserCustom

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserCustom
        fields = '__all__'