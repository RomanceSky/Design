# from django.conf.urls import url, include
# import accounts.views
# from rest_framework.routers import DefaultRouter
# from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns
# from accounts import views
# from rest_framework import renderers
# from rest_framework.schemas import get_schema_view
# from knox import views as knox_views
# from accounts.views import *
#
# schema_view = get_schema_view(title='Pastebin API')
#
# app_name = "accounts"
#
# accounts_router = DefaultRouter()
# accounts_router.register(r'^(?P<id>[0-9]+)/users', accounts.views.UserViewSet,
#                  base_name='user')
# accounts_router.register(r'groups', accounts.views.GroupViewSet)
#
# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLS for the browsable API.
# urlpatterns = accounts_router.urls
#
# urlpatterns = [
#     # url(r'login/', LoginView.as_view(), name='knox_login'),
#     # url(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
#     # url(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
#     url(r'^schema/$', schema_view),
#     url(r'^$', views.api_root),
# #    url(r'^myaccounts/(?P<pk>[0-9]+)/highlight/$', views.MyaccountsHighlight.as_view(), name='myaccounts'),
#     # url(r'^', include(accounts_router.urls)),
# ]
