# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class job(models.Model):
    image=models.ImageField(Upload_to='images/')
    summary=models.CharField(max_length=200)
