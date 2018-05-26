from django.db import models

# Create your models here.

class MyUsers(models.Model):
    groups = models.ForeignKey(
        'Group',
        null=False,
        blank=False,
        related_name='groups',
        on_delete=models.PROTECT
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

class Group(models.Model):
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
