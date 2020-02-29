from django import forms

from .models import *


# TODO: Put your dog questions form here
class DogForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'daily_walk': forms.CheckboxInput,
        }
        labels = {
            'email': 'Please provide an Email address to receive results.',
            'age': 'How old is your dog?',
            'breed': 'What is the breed of your dog?',
            'daily_walk': 'Do you walk your dog daily?',
        }

    SIT = 'Sit'
    FETCH = 'Fetch'
    STAY = 'Stay'
    ROLLOVER = 'Rollover'
    NONE = 'None'
    TRICK_CHOICES = [
        (SIT, 'Sit'),
        (FETCH, 'Fetch'),
        (STAY, 'Stay'),
        (ROLLOVER, 'Roll Over'),
        (NONE, 'None. It is okay. My pup was stubborn too.'),
    ]
    trick = forms.MultipleChoiceField(
        choices=TRICK_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='What tricks does your dog know? Select all that apply:'
    )
