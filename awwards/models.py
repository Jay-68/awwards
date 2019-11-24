# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='profile_pics/', default='No Image')
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


class Project(models.Model):
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='project_pictures/')
    description = HTMLField()
    link = models.URLField()
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def avg_design(self):
        design_reviews = list(map(lambda x: x.design, self.review_set.all()))
        return np.mean(design_reviews)

    def avg_content(self):
        content_reviews = list(map(lambda x: x.content, self.review_set.all()))
        return np.mean(content_reviews)

    def avg_usability(self):
        usability_reviews = list(
            map(lambda x: x.usability, self.review_set.all()))
        return np.mean(usability_reviews)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def project_by_id(cls, id):
        project = Project.objects.filter(id=id)
        return project

    @classmethod
    def get_projects(cls):
        projects = Project.objects.all()
        return projects

    class Meta:
        ordering = ['-timestamp']
