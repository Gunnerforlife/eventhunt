from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.email)