from django.db import models
from rest_framework.serializers import ModelSerializer
from estudiantes.models import Estudiante

class EstudianteSerializer(ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'