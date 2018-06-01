from django.contrib.auth.models import User, Group
from rest_framework import serializers
from accounts.models import Ip
from rest_framework.response import Response

from datetime import datetime
from rest_framework.renderers import  JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO


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


class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    
    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance

comment = Comment('1111@qq.com', content='foo bar')
serializer = CommentSerializer(comment)
s = serializer.data
json = JSONRenderer().render(s)

stream = BytesIO(json)
data = JSONParser().parse(stream)
print(data)
serializer = CommentSerializer(data=data)
serializer.is_valid()
k = serializer.validated_data
print(k)
# result
# {'email': '1111@qq.com', 'content': 'foo bar', 'created': '2018-06-01T02:31:54.901793Z'}
# OrderedDict([('email', '1111@qq.com'), ('content', 'foo bar'),
# ('created', datetime.datetime(2018, 6, 1, 2, 31, 54, 901793, tzinfo=<UTC>))])
#
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
