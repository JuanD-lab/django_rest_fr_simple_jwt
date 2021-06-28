from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from estudiantes.models import Estudiante
from estudiantes.serializer import EstudianteSerializer
# Create your views here.
class Estudiantes(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer