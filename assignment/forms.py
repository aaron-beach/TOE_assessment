from django import forms
from assignment.models import *


# TODO: Put your dog questions form here
class DogForm(forms.Form):
    daily_walk = forms.BooleanField(label='Do you walk your dog daily?', required=False)
    dog_breed = forms.CharField(
        label='What is the breed of your dog?',
        max_length=40,
        empty_value='',
        strip=True
    )
    dog_age = forms.IntegerField(label='How old is your dog?', max_value=30)
    dog_tricks = forms.ModelMultipleChoiceField(
        label='What tricks does your dog know? Select all that apply:',
        queryset=Trick.tricks.all().order_by('name'),
        required=False
    )
    user_email = forms.CharField(
        label='Please provide an Email address to receive results.',
        max_length=50,
        required=True
    )
