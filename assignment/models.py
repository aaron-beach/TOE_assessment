from django.db import models
from django.contrib.postgres.fields import ArrayField

# TODO: Put your dog questions model here


def arrayfield_default_value():
    return "NA"


class Pet(models.Model):
    daily_walk = models.NullBooleanField()
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=30, blank=True)
    trick = ArrayField(models.CharField(max_length=20), default=arrayfield_default_value)
    email = models.CharField(max_length=200, blank=True)
