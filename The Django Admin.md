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

 
>>> from django.contrib.auth.hashers import check_password
>>> from django.conf import settings
>>> from django.contrib.auth.models import User
>>> class SettingsBackend:
...      # 验证用户名和密码的后端
...     def authenticate(self, request, username=None, password=None):
...         login_valid = (settings.ADMIN_LOGIN == username)
...         pwd_valid  = check_password(password_, settings.ADMIN_PASSWORD)
...         if login_valid  and pwd_valid:
...             try:
...                 user = User.objects.get(username=username)
...             except User.DoesNotExist:
...                 # 创建一个新的用户, 不需要设置密码，因为只有settings.py中的
... # 密码才可以被check
...                 user = User(username=username)
...                 user.is_staff = True
...                 user.is_superuser = True
...                 user.save()
...             return user
...         return None
...     def get_user(self, user_id):
...         try:
...             return User.objects.get(pk=user_id)
...         except User.DoesNotExist:
...             return None
...
>>> s = '俊'
>>> p = '123'
>>> s1 = SettingsBackend
>>> s1.authenticate(s,p)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "<console>", line 4, in authenticate
  File "/Users/charolim/MyDesign/Desginenv/lib/python3.6/site-packages/django/conf/__init__.py", line 57, in __getattr__
    val = getattr(self._wrapped, name)
AttributeError: 'Settings' object has no attribute 'ADMIN_LOGIN'
>>>
```
