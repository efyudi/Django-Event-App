# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Venue(models.Model):
    name = models.CharField(verbose_name="Venue Name", max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(verbose_name="Zip/Postal Code", max_length=10)
    phone = models.CharField(
        verbose_name="Phone Number", max_length=11, blank=True)
    email_address = models.EmailField(verbose_name="Email Address", blank=True)
    website = models.URLField(verbose_name="Website", blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(verbose_name="Event Name", max_length=120)
    event_date = models.DateTimeField(verbose_name="Event Date")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
