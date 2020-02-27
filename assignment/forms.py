from django import forms

from .models import *


# TODO: Put your dog questions form here
class DogForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        labels = {
            'email': 'Please provide an Email address to receive results.',
            'tricks': 'What tricks does your dog know? Select all that apply:',
            'age': 'How old is your dog?',
            'breed': 'What is the breed of your dog?',
            'daily_walk': 'Do you walk your dog daily?'
        }
