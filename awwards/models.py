# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

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


class Review(models.Model):
    REVIEW_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )

    design = models.IntegerField(
        choices=REVIEW_CHOICES, default=0, blank=False)
    usability = models.IntegerField(
        choices=REVIEW_CHOICES, default=0, blank=False)
    content = models.IntegerField(
        choices=REVIEW_CHOICES, default=0, blank=False)
    average = models.DecimalField(
        default=1, blank=False, decimal_places=2, max_digits=40)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.user

    # saving and deleteing the choices
    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()