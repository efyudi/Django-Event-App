# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Venue, Event

# Register your models here.


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    #fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    fieldsets = (('Required information', {'description': 'These are the required fields', 'fields': (('name', 'venue'), 'event_date')}),
                 ('Optional Fields', {'classes': ('collapse',), 'fields': ('description', 'manager')}))
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)

    # admin.site.register(Venue) #Another way of registering the models in admin view
    # admin.site.register(Event)
