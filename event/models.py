from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=120, null=False, blank=False)
    user = models.ForeignKey(User, default=None)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)