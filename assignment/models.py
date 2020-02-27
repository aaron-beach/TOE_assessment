from django.db import models


# TODO: Put your dog questions model here
class Trick(models.Model):
    """
    Tricks receives it's own model to allow flexibility and scalability.
    """
    name = models.CharField(max_length=200, primary_key=True)
    tricks = models.Manager()

    def __str__(self):
        return self.name


class Pet(models.Model):
    """
    Pet model represents a dog. I have purposely used Pet to allow future scalability to the forms
    to additional pets.
    """
    daily_walk = models.NullBooleanField()
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=30)
    tricks = models.ManyToManyField(Trick)
    email = models.CharField(max_length=200, blank=True)

