from django.db import models
# from accounts.models import Myaccounts
from django.contrib.auth import get_user_model

# Create your models here.
class Purchase(models.Model):
    purchaser = models.CharField(
            null=False,
            blank=False,
            max_length=125,
    )
    # name = models.ForeignKey(
    #     'get_user_model',
    #     null=False,
    #     blank=False,
    #     related_name='purchases',
    #     on_delete=models.CASCADE
    # )
