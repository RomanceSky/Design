# Create your views here.
from rest_framework import viewsets, permissions, filters, status
from accounts.serializers import MyUsersSerializer, GroupSerializer
from accounts.models import MyUsers, Group

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing and creating chapters
    """
    queryset = MyUsers.objects.all()
    serializer_class = MyUsersSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
