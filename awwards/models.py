# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='profile_pics', default='No Image')
    bio = HTMLField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    contact = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter_by(user=id).first()

        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)

        return profile
