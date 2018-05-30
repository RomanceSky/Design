示例后端，它对在您的设置中定义的用户名和密码变量进行身份验证。

settings.py 文件并创建一个Django用户对象 User object，这是用户首次验证
 
Changed in Django 1.11:

The request parameter was added to authenticate() and support for backends that don’t accept it will be removed in Django 

代码

```
  """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.

    Use the login name and a hash of the password. For example:

    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M='
    """
class SettingsBackend:
      # 验证用户名和密码的后端
     def authenticate(self, request, username=None, password=None):
         login_valid = (settings.ADMIN_LOGIN == username)
         pwd_valid  = check_password(password, settings.ADMIN_PASSWORD)
         if login_valid  and pwd_valid:
             try:
                 user = User.objects.get(username=username)
             except User.DoesNotExist:
                 # 创建一个新的用户, 不需要设置密码，因为只有settings.py中的
 # 密码才可以被check
                 user = User(username=username)
                 user.is_staff = True
                 user.is_superuser = True
                 user.save()
             return user
         return None
     def get_user(self, user_id):
         try:
             return User.objects.get(pk=user_id)
         except User.DoesNotExist:
             return None

ADMIN_LOGIN = 'admin'
ADMIN_PASSWORD = 'pbkdf2_sha256$30000$Vo0VlMnkR4Bk$qEvtdyZRWTcOsCnI/oQ7fVOu1XAURIZYoOZ3iq8Dr4M'

s1 = SettingsBackend
s1.authenticate('1','2')
s1.authenticate('俊','122')
  login_valid = (ADMIN_LOGIN == username)
  pwd_valid  = check_password(password, ADMIN_PASSWORD)
    
```

注意：

get_user 方法只接受一个参数``user_id``，user_id 有可能是 用户名、数据库 ID 或者其它任何值（该值必须是用户对象的主键），该方法返回一个用户对象。

```
views.py

def authenticate(request=None, **credentials):
    from django.contrib.auth import authenticate
    if django.VERSION < (1, 11):
        return authenticate(**credentials)
    else:
        return authenticate(request=request, **credentials)

serializers.py
    def get_user(self, obj):
        user = obj.order.user
        if not user.address:
            raise FileNotFoundError
        return {
            'name': user.first_name + ' ' + user.last_name, 'address': user.address, 'email': user.email
        }
```
