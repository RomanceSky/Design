from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser


class MyUsers(models.Model):
    #REQUIRED_FIELDS = ('name',)
    #USERNAME_FIELD = ('name')
    groups = models.ForeignKey(
        'Groups',
        null=False,
        blank=False,
        related_name='myusers',
        on_delete=models.CASCADE
    )
    name = models.CharField(
            null=False,
            blank=False,
            max_length=125,
    )
    email = models.EmailField(
            null=False,
            blank=False,
            max_length=125,
    )

    url = models.URLField(
            null=False,
            blank=True,
            max_length=125,
    )


class Groups(models.Model):
    name = models.CharField(
            null=False,
            blank=False,
            max_length=125,
    )

    url = models.URLField(
            null=False,
            blank=True,
            max_length=125,
    )

class Ip(models.Model):
    user = models.ForeignKey(
        'MyUsers',
        null=False,
        blank=False,
        related_name='ips',
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        'Groups',
        null=False,
        blank=True,
        related_name='ips',
        on_delete=models.CASCADE
    )
    ip_addr = models.GenericIPAddressField(
        blank=False,
        null=False,
    )
