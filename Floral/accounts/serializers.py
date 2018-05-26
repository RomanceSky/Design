from rest_framework import serializers
from accounts.models import MyUsers, Group
from rest_framework import serializers


class MyUsersSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    # answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = MyUsers
        fields = ('id', 'name', 'url', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')

    # New Features
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance
    #
    # def create(self, validated_data):
    #     return MyUsers.objects.create(**validated_data)
