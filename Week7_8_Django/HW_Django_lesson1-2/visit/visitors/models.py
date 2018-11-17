from django.db import models


class Visitor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    some_info = models.CharField(max_length=1000)
