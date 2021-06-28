from rest_framework.viewsets import ModelViewSet
from materias.models import Materia
from materias.serializer import MateriaSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# Create your views here.
class Materias(ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permissions = (AllowAny, )
        elif self.request.method =='DELETE':
            permissions = (IsAdminUser, )
        else:
            permissions = (IsAuthenticated, )
            
        return [permission() for permission in permissions]