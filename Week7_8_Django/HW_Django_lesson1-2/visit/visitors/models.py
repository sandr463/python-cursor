from django.db import models
from django.conf import settings


class Visitor(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    age = models.IntegerField()
    some_info = models.CharField(max_length=1000)
