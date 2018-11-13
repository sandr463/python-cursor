from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    author = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
