from django.db import models


# TODO: Put your dog questions model here
class Pet(models.Model):

    SIT = 'SI'
    FETCH = 'FT'
    STAY = 'ST'
    ROLLOVER = 'RO'
    NONE = 'NA'
    TRICK_CHOICES = [
        (SIT, 'Sit'),
        (FETCH, 'Fetch'),
        (STAY, 'Stay'),
        (ROLLOVER, 'Roll Over'),
        (NONE, 'It is okay. My pup was stubborn too'),
    ]
    trick = models.CharField(
        max_length=2,
        choices=TRICK_CHOICES,
        default=NONE,
    )
    daily_walk = models.NullBooleanField()
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=200, blank=True)
