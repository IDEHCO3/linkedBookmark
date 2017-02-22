from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LinkedBookmarkResource(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=True)
    user = models.ForeignKey(User, null=False, related_name='linkedBookmarks')

class LinkedBookmarkItemResource(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=True)
    iri = models.URLField(blank=False, null=False)
    linkedBookmark = models.ForeignKey(LinkedBookmarkResource, null=False, related_name='items')
