from django.db import models


class Project(models):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)


class Blog(models):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
