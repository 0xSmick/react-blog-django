from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage, FileSystemStorage
import datetime

#def file_save

class Books(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now)
    title = models.CharField(max_length=100, blank=False, default='foo')
    user = models.ForeignKey(User, related_name="owner_podcasts", null=True)
    bookFile = models.FileField(null=True, upload_to='uploads/')
