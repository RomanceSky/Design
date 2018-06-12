from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from accounts.serializers import UserSerializer, GroupSerializer, CommentListSerializer,IpSerializer, CommentSerializer,CreateUserSerializer,CardSerializer,MemberSerializer
# AdmireSerializerfrom rest_framework.authtoken.models import Token
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.models import Ip, Comment, Admire, Card, Member
from rest_framework import status

from rest_framework.renderers import  JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
"""
class CustomMixin(viewsets.ModelViewSet):
    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )

    def admin_permissions(self, actions):
        if self.action in actions:
            self.permission_classes = [permissions.IsAuthenticated, ]
            print(self.__class__)
        return super(self.__class__, self).get_permissions()
"""

class CreateCardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

class CreateMemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (AllowAny,)
    queryset = User.objects.all().order_by('-date_joined').prefetch_related('groups')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        auth_token = AuthToken.objects.create(user)
        # print(auth_token)
        return Response(
            {
                "email": user.email,
                "token": auth_token,
                "id": user.id,
                #"key": auth_token.key,
            }
        )


        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.token = AuthToken.objects.create(user)
        print(request.user)
        self.headers = self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        # token is setted into the requested headers
        # token = Token.objects.create(user=user)
        print(self.token.key)
        """


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     允许用户查看或编辑的API路径。
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     def Post(self, request, *args, **kwargs):
#                 serializer = self.get_serializer(data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 user = serializer.save()
#                 token = Token.objects.create(user=user)
#                 print(token.key)
#                 # auth_token = AuthToken.objects.create(user)
#                 # print(auth_token.key)
#                 return Response(
#                         {
#                             "name": user.username,
#                             "token": token,
#                             "id": user.id,
#                         }
#                 )
#

class CreateUserViewSet(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class IpViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Ip.objects.all()
    serializer_class = IpSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # serializer_class = CommentListSerializer


    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data, many=True)
        # json = JSONRenderer().render(serializer)
        # stream = BytesIO(json)
        # data = JSONParser().parse(stream)
        # print(serializer)
        # # result
        # < QueryDict: {'username': ['charolim11']} >
        # CommentSerializer(data= < QueryDict: {'username': ['charolim11']} >):
        # email = EmailField()
        # content = CharField(max_length=200)
        # created = DateTimeField()

        if serializer.is_valid(raise_exception=True):# 如果数据无效就返回400响应
            # comment = serializer.save(user=request.user)
            comment = serializer.save()

            # print(comment)
            # CommentSerializer(data={}):
            # email = EmailField()
            # content = CharField(max_length=200)
            # created = DateTimeField()

        # upon is serializer, down is deserializer
        return Response(serializer.data)

"""

class AdmireViewSet(viewsets.ModelViewSet):
    serializer_class = AdmireSerializer
    queryset = Admire.objects.all()

    # Serialize multiple objects
    queryset = Admire.objects.all()
    serializer = AdmireSerializer(queryset, many=True)
    serializer.data


    # Deserialize multiple objects

    def create(self, request, *args, **kwargs):
        # payment_method = request.data.get('payment_method')
        payment_method = request.query_params.get('payment_method')

        try:# int() argument must be a string, a bytes-like object or a number, not 'AnonymousUser'
            admire = Admire.objects.get(user_id=request.user.id)
        except Admire.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if admire.status == Admire.SUCCEED:
            return Response('The admire has been paid.', status=status.HTTP_400_BAD_REQUEST)
        if admire.expired_at < now():
            admire.status = Admire.FAILED
            admire.save()
            return Response('The paymenet of admire is failured.', status=status.HTTP_400_BAD_REQUEST)
"""

# # Create your views here.
# from rest_framework import viewsets, permissions, filters, status
# from rest_framework import mixins
# from rest_framework.views import APIView
# from rest_framework import generics
# from django.shortcuts import get_object_or_404
# # from rest_framework.permissions import IsAdmin
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight
# from rest_framework import viewsets
# from rest_framework import permissions
# from accounts.permissions import IsOwnerOrReadOnly
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
# from rest_framework import renderers
# from rest_framework.response import Response
# from accounts.serializers import MyUsersSerializer, GroupSerializer
# from accounts.models import MyUsers, Group
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from knox.auth import TokenAuthentication
# from knox.views import LoginView as KnoxLoginView
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.http import HttpResponseRedirect
# import os
#
# from rest_framework.authtoken.models import Token
#
# permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly
#                             )
#
# def admin_permissions(self, actions):
#     if self.action in actions:
#         self.permission_classes = [permissions.IsAuthenticated, ]
#     return super(self.__class_, self).get_permissions()
#
# class LoginView(KnoxLoginView):
#     authentication_classes = [BasicAuthentication]
#
# class ExampleView(APIView):
#     authentication_classes = (
#                 TokenAuthentication,
#     )
#     """
#     permission_classes = (
#                 permissions.IsAuthtenticated,
#     )
#     """
#     def get(self, request, format=None):
#         content = {
#             'foo': 'bar'
#         }
#         return Response(content)
# def authenticate(request, **credentials):
#     from django.contrib.auth import IsAuthenticate
#     if django.VERSION < (1, 11):
#         return authenticate(**credentials)
#     else:
#         return authenticate(request=request, **credentials)
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = MyUsers.objects.all()
#     serializer_class = MyUsersSerializer
#
#
#     def retrieve(self, request, *args, **kwargs):
#         print(request.user) # show AnonymousUser
#         print(self.kwargs['id'])
#         myaccounts = get_object_or_404(self.get_queryset(), id=kwargs['id'])
#         name = Myaccounts.objects.get(id=kwargs['id'])
#         print(name.id)
#         serializer = MyaccountsSerializer(myaccounts)
#         # return Response(dict(data=(serializer.data), name=name.name.upper()))
#         # api = request.get_host() + '/api/v1/accounts/{}'.format(kwargs['id'])
#         # print(type(api))
#         # print(type(MyaccountsSerializer(instance=name)))
#
#         # print(os.getenv('HOMEPAGE_DOMAIN'))
#         # url = 'http://' + os.environ.get('HOMEPAGE_DOMAIN') + api
#         # print(url)
#         # return HttpResponseRedirect(url)
#         return Response(MyaccountsSerializer(instance=name).data)
#
#
#
#         def create(self, request, *args, **kwargs):
#             serializer = self.get_serializer(data=request.data)
#             srializer.is_valid(raise_exception=True)
#             user = serializer.save()
#             token = Token.objects.create(user=user)
#             print(token.key)
#             # auth_token = AuthToken.objects.create(user)
#             # print(auth_token.key)
#             # return Response(
#             #         {
#             #             "name": user.name,
#             #             "token": auth_token,
#             #             "id": user.id,
#             #         }
#             # )
#
#
# """
#
#     def create(self, request, *args, **kwargs):
#         user_id = request.query_params.get('name')
#         print(dict(name=user_id))
#         # print(user_id)
#         # name = Myaccounts.objects.get(name=user_id)
#         print(request.data)
#         # myaccounts = Myaccounts.objects.create(name=user_id, url=)
#         return Response({'1':request.data.get('name'), '2': request.data.get('url')}
#
# """
#
# """
#     def get_queryset(self):
#         if self.request.user.user_role == User.STUDENT:
#             try:
#                 self.queryset = self.queryset.filter(received_by=self.request.user, is_deleted=False)
#             except FieldError:
#                 self.queryset = self.queryset.filter(created_by=self.request.user, is_deleted=False)
#         return super(DefaultsMixin, self).get_queryset()
#
# """
#
# """
#     def create(self, request, *args, **kwargs):
#         name = request.data.get('name')
#         print(name)
#         print(request.data)
#         myaccounts_id = request.data.get('myaccounts_id')
#         defaults = dict(id=myaccounts_id)
#         serializer = MyaccountsSerializer(instance=Myaccounts)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
# """
#
#
# # Creating an endpoint for the highlighted snippets
# class MyUsersHighlight(generics.GenericAPIView):
#     queryset = MyUsers.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         # print(request.query_params(id))
#         # print(request.get(id))
#         myusers = self.get_object()
#         print(myusers)
#         # return Response(myaccounts.highligted)
#         return response('xixi')
#
#
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'MyUsers': reverse('users:myusers', args=(1,),request=request, format=format),
#         # 'Group': reverse('')
#     })
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
#
# class BlacklistPermission(permissions.BasePermission):
#     """
#     Global permission check for blacklisted IPs.
#     """
#     def has_permission(self, request, view):
#         ip_addr = request.META['REMOTE_ADDR']
#         # blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
#         return not blacklisted
#
# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # Instance must have an attribute named `owner`.
#         return obj.owner == request.user
