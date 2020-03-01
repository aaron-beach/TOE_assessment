import re

from django.core.mail import send_mail
from django.db import models
from django.contrib.postgres.fields import ArrayField
from toe_hiring_2020.settings import DEFAULT_FROM_EMAIL


def arrayfield_default_value():
    return "NA"


class Pet(models.Model):
    """
    Class used to represent a Pet/Dog.
    This will be used to create form and view.

    Attributes:
    ---
    daily_walk: Bool
        whether dog gets daily walk.
    age: int
        age of a pet
    breed: str
        breed of a pet. allows blank if user doesn't know
    trick: arr 
        the tricks a pet can perform
    email: str
        user email for email results. can be blank if user doesn't want to receive response

    Methods:
    ---
    email_user(form)
        sends email with results to user    
    """
    daily_walk = models.NullBooleanField()
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=30, blank=True)
    trick = ArrayField(models.CharField(max_length=20), default=arrayfield_default_value)
    email = models.CharField(max_length=200, blank=True)

    def email_user(self):
        """
        Sends an email to this User.
        """
        subject = 'Thank you!'

        def email_message(form_response):
            """
            Formatting the message to be readable by users.
            """
            message = f'Thank you for taking the time to fill out the form. \n'

            # Pretty message for walk boolean
            is_walked = form_response.cleaned_data['daily_walk']
            if is_walked:
                message += f'Your dog loves the walks! Trust us. \n'
            else:
                message += f'Hope you have a fenced in yard.\n'

            # If a breed isn't supplied shouldn't be added to message
            breed = form_response.cleaned_data["breed"]
            if len(breed) != 0 or breed.isspace():
                message += f'{breed}s are so cute!!\n'

            # age based message logic
            age = form_response.cleaned_data['age']
            age_message = f'{age} years old. '
            if age < 2:
                age_message += f'Still a puppy. \n'
            elif age > 9:
                age_message += f'An old friend. \n'
            else:
                age_message += f'Prime of their life! \n'
            message += age_message

            # Tricky trick message. Need to spend more time on the "None" logic
            trick = form_response.cleaned_data['trick']
            trick_message = 'Tricks: \n'
            is_none = re.split(r"(\b[\w']+\b)(?:.+|$)", trick[0])[1] 

            if len(trick) > 1:
                for i in trick:
                    trick_message += f'{i}\n'
                trick_message += f'Impressive list. You must work really hard.'
            elif is_none:
                trick_message += f'{"It is okay. Tricks are not for everyone" if age > 2 else "There is still time keep trying!"}'
            else:
                trick_message += f'{trick[0]}\n Great start!'
            message += trick_message

            return message

        send_mail(subject, email_message(self), DEFAULT_FROM_EMAIL,
                  [self.cleaned_data['email'], 'admin@dogstartup.com'],
                  fail_silently=False)
