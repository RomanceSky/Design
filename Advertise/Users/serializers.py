from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = ('url', 'name', 'user')
    # serializer and de-serializer
    def get_order(self, obj):
        user = obj.user
        return {'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'email': obj.email,
                'ordered': user.data_created.strftime('%Y-%m-%d %H:%M:%S'), 'price': format(order.total_amount, '0,.2f'),
                }
