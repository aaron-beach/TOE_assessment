from django import forms

from .models import *


class DogForm(forms.ModelForm):
    """
    Class used to define a Pet form 
    """
    class Meta:
        model = Pet
        fields = '__all__'
    # daily_walk question field widget for a checkbox
        widgets = {
            'daily_walk': forms.CheckboxInput,
        }
    # labeling for the form fields    
        labels = {
            'email': 'Please provide an Email address to receive results.',
            'age': 'How old is your dog?',
            'breed': 'What is the breed of your dog?',
            'daily_walk': 'Do you walk your dog daily?',
        }
    # Define options for a Trick
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
    # Define the trick field as a multiple choice form. Apply Tricks defined above.
    trick = forms.MultipleChoiceField(
        choices=TRICK_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='What tricks does your dog know? Select all that apply:'
    )
