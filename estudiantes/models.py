from django.db import models
from materias.models import Materia
# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    materias = models.ManyToManyField(
        Materia,
        related_name='estudiantes'
    )

    def __str__(self):
        return self.nombre
