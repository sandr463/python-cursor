from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


class Visitor(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    age = models.IntegerField()
    some_info = RichTextUploadingField(null=True, blank=True)
