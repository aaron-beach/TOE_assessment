from django.db import models


# TODO: Put your dog questions model here


class User(models.Model):
    user_email = models.CharField(max_length=200)


class Trick(models.Model):
    name = models.CharField(max_length=200)
    tricks = models.Manager()


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    breed = models.CharField(max_length=30)
    tricks = models.ManyToManyField(Trick)
