from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response

# from datetime import datetime
# from disposable_email_checker.validators import validate_disposable_email
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email as django_validate_email

from accounts.models import Comment, Ip, MyUsers, Admire, Card, Member


class MemberSerializer(serializers.ModelSerializer):
    cards = serializers.PrimaryKeyRelatedField(many=True, queryset=Card.objects.all()) # read_only=True
    class Meta:
        model = Member
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    # member = serializers.PrimaryKeyRelatedField(read_only=True)
    member = MemberSerializer(required=False)
    class Meta:
        model = Card
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class IpSerializer(serializers.HyperlinkedModelSerializer):

    # SerializerMethodField（）： Serialization and deserialization

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

"""
class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
"""
# Parent

class CommentListSerializer(serializers.ListSerializer):

    class Meta:
        model=Comment
        fields = ('email', 'content', 'created', 'user', 'groups')

    @classmethod
    def many_init(cls, *args, **kwargs):
        # 实例化子序列化器类。
        kwargs['child'] = cls()
        # 实例化列表序列化父类
        return CommentListSerializer(*args, **kwargs)

    def create(self, validated_data):
        s = [Comment(**item) for item in validated_data]
        print(s)
        # result
        # s=()
        return Comment.objects.bulk_create(s)



# Child
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    user = serializers.PrimaryKeyRelatedField(
        queryset=MyUsers.objects.all()
    )
    # groups = serializers.PrimaryKeyRelatedField(
    #     queryset=MyUsers.objects.all()
    # )
    # ip = IpSerializer
    # groups = GroupSerializer
    # #
    # # Field level validation
    # def validated_email(self, value):
    #     """Validate a single email."""
    #     if not value:
    #         return False
    #     # Check the regex, using the validate_email from django.
    #     try:
    #         django_validate_email(value)
    #     except ValidationError:
    #         return False
    #     else:
    #         # Check with the disposable list.
    #         try:
    #             validate_disposable_email(value)
    #         except ValidationError:
    #             return False
    #         else:
    #             return True

    # # Object level validation
    # def validate(self, value):
    #     """
    #     Check that the email is before the content
    #     """
    #     if value['email'] > value['content']:
    #         raise serializers.ValidationError("email must occur after content")
    #     return value
    # # result
    # # {
    # #     "non_field_errors": [
    # #         "email must occur after content"
    # #     ]
    # # }


    class Meta:
        model=Comment
        fields = ('email', 'content', 'created', 'user')

    # class Meta:
    #     list_serializer_class = CommentListSerializer


    def create(self, validated_data):
        ip_data = validated_data.pop('ip')
        comment = Comment.objects.create(**validated_data)
        Ip.objects.create(comment=comment, **ip_data)
        return Comment.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


class MyUsersSerializer(serializers.HyperlinkedModelSerializer):
    # myaccounts = serializers.PrimaryKeyRelatedField(read_only=True)
    myusers = serializers.StringRelatedField(source='groups.name')
    # highlight = serializers.HyperlinkedIdentityField(view_name='accounts:myaccounts', format='html'
    groups = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all()
    )

    class Meta:
        model = MyUsers
        fields = ('id', 'name', 'email', 'url', 'groups', 'myusers')
        # You need a way to determine which views can apply hyperlinks to model instances.
        extra_kwargs = {
            'url': {'view_name': 'myusers', 'lookup_field': 'email'},
            'users': {'lookup_field': 'username'}
        }
"""
class AdmireSerializer(serializers.ModelSerializer):
# if a nested associated field can receive a list,
# the many=True flag should be passed to the nested serializer.
    # user = MyUsersSerializer()
    # content = IpSerializer(many=True)
    # content = serializers.CharField(many=True)
    # admire_ammount = serializers.SerializerMethodField()
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    # user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Admire
        fields = '__all__'
        # fields = (

    #     # )
    # serializer = MyUsersSerializer(MyUsers, context={'request': request})
    # serializer.data
    #
    # def get_total_amount(self, obj):
    #     try:
    #         return Admire.objects.get(user=self.context.get('request').user).total_amount
    #     except Admire.DoesNotExist:
    #         return ''
    def get_status_display(self, obj):
        return obg.get_status_display()

    def create(self, validated_data):
        admires1 = [Admire(**item) for item in validated_data]
        s = Admire(**validated_data)
        print(s)
        print(admires1)
        user_data = validated_data.pop('user')
        admire = Admire.objects.create(*validated_data)
        MyUsers.objects.create(**user_data)
        return admire

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.status = validated_data.get('status', instance.status)
        instance.save()

        user.is_premium_member = user_data.get(
            'is_user_member',
            user.is_premium_member
        )

        user.has_suppport_contract = user_data.get(
            'has_support_contract',
            user.has_support_contract
        )
        user.save()

        return instance
"""
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# # Customize the ListSerializer behavior
# Complete process
# class CustomListSerializer(serializer.ListSerializer):
#     ...
# class CustomSerializer(serializers.Serializer):
#     ...
#     class Meta:
#         list_serializer_class = CustomListSerializer
#
# Customize the creation of multiple objects

class BookListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        books = [Book(**item) for item in validated_data]
        return Book.objects.bulk_create(books)




#
# class EnventSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     room_number = serializers.IntegerField(choices=[1,2,3])
#     date =serializers.DateField()
#
#     class Meta:
#         # There can only be one activity per room per day.
#         validators = UniqueTogetherValidator(
#             queryset = Envent.objects.all(),
#             fields = ['room_number', 'date']
#         )

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
