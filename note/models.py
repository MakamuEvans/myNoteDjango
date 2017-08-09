# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=250, null=True)
    note = models.CharField(max_length=250, null=True)
    favourite = models.BooleanField(max_length=250)
    imageurl = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' ' + self.note
