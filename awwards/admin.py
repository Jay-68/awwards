# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from awwards.models import Profile, Project, Review

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Review)