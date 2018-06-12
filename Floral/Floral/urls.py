# """Floral URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include, url
# from rest_framework.documentation import include_docs_urls
# from django.conf.urls import url, include
#
# # router.register(r'groups', views.GroupViewSet)
#
# # URL Patterns
# urlpatterns = [
#     # url(r'api/auth/', include('knox.urls')),
#     # path('admin/', admin.site.urls),
#     url(r'^docs/', include_docs_urls(title='My API title',  public=False)),
#     url(r'^api/v1/accounts/', include('accounts.urls', namespace='accounts')),
#     url(r'^auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
#
#
# ]
from django.conf.urls import url, include
from rest_framework import routers
from accounts import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'ips', views.IpViewSet)
router.register(r'comments', views.CommentViewSet)
#router.register(r'admires', views.AdmireViewSet)
router.register(r'createusers', views.CreateUserViewSet)
router.register(r'cards', views.CreateCardViewSet)
router.register(r'members', views.CreateMemberViewSet)


# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
    url(r'api/auth/', include('knox.urls')),
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]