# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from tardis.tardis_portal.models import Dataset

@python_2_unicode_compatible
class Equipment(models.Model):
    key = models.CharField(unique=True, max_length=30)
    dataset = models.ManyToManyField(Dataset, blank=True)
    description = models.TextField(blank=True)
    make = models.CharField(max_length=60, blank=True)
    model = models.CharField(max_length=60, blank=True)
    type = models.CharField(max_length=60, blank=True)
    serial = models.CharField(max_length=60, blank=True)
    comm = models.DateField(null=True, blank=True)
    decomm = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.key
