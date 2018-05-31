from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import Ip
from rest_framework.response import Response

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'user')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class IpSerializer(serializers.HyperlinkedModelSerializer):
    #SerializerMethodField（）： Serialization and deserialization
    group = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Ip
        fields = ('user',  'ip_addr', 'group')

    def get_group(self, obj):
        group = obj.group
        return{'url': group.url,
               'name': group.name,
              }

    def get_user(self, obj):
        user = obj.user
        if user:
            print(1)
        return {
            'name': user.name + ' ' + 'hello'
        }

    def get_attribute(self, instance):
        a = instance
        print(a)
        return instance

# from rest_framework import serializers
# from rest_framework import status
#
# from accounts.models import MyUsers, Group
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     group = serializers.SerializerMethodField()
#     class Meta:
#         model = Group
#         fields = ('id', 'url', 'name')
#     def get_group(self, obj):
#         user = obj.group.username
#         if not name.address:
#               raise FileNotFoundError
#         return {
#             'name': user.username
#         }
#
# class MyUsersSerializer(serializers.HyperlinkedModelSerializer):
#     # myaccounts = serializers.PrimaryKeyRelatedField(read_only=True)
#     myaccounts = serializers.StringRelatedField(source='groups.name')
#     # highlight = serializers.HyperlinkedIdentityField(view_name='accounts:myaccounts', format='html'
#     groups = serializers.PrimaryKeyRelatedField(
#         queryset=Group.objects.all()
#     )
#
#     class Meta:
#         model = MyUsers
#         fields = ('id', 'name', 'email', 'url', 'groups', 'myusers')
