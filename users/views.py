from rest_framework.viewsets import ModelViewSet
from users.models import UserCustom
from users.serializer import UserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# Create your views here.
class Users(ModelViewSet):
    queryset = UserCustom.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            permissions = (AllowAny, )
        elif self.request.method =='DELETE':
            permissions = (IsAdminUser, )
        else:
            permissions = (IsAuthenticated, )
            
        return [permission() for permission in permissions]