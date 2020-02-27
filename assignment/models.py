from django.db import models


# TODO: Put your dog questions model here


class DogOwner(models.Model):
    """
    DogOwner is separated from the pet to allow a one to many relationship between
    owners and pets.
    """
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email


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
    owner = models.ForeignKey(DogOwner, on_delete=models.CASCADE)
    daily_walk = models.NullBooleanField()
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=30)
    tricks = models.ManyToManyField(Trick)


