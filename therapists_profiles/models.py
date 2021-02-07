"""Define ORM models here"""

from django.db import models


# Create your models here.
class Therapist(models.Model):
    """Model for keeping therapists information"""
    airtable_id = models.CharField(max_length=100, default=None)
    name = models.CharField(default=None, null=True, max_length=100)
    photo_url = models.CharField(default=None, null=True, max_length=100)


class Method(models.Model):
    """Model for keeping methods related to therapists"""
    name = models.CharField(max_length=100, default=None)
    therapist = models.ManyToManyField(Therapist)
