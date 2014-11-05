from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from event.models import Event
# Create your models here.

class Eve_Upvote(models.Model):
    user = models.ManyToManyField(User)
    event = models.ForeignKey(Event)
    total_upvotes = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.event)