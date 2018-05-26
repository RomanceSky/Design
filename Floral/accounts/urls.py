from django.conf.urls import url, include
import accounts.views
from rest_framework.routers import DefaultRouter
from rest_framework import routers

app_name = "accounts"

accounts_router = DefaultRouter()
accounts_router.register(r'users', accounts.views.UserViewSet,
                 base_name='accounts_user')
accounts_router.register(r'groups', accounts.views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLS for the browsable API.
urlpatterns = [
    # url(r'^accounts/', include(accounts_router.urls))
    url(r'^', include(accounts_router.urls)),
    # rl(r'^', include(router.urls)),
    # 就是 router.DefaultRouter赋值给的router(此处是accounts_router)
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
