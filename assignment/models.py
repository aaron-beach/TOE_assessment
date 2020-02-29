import re

from django.core.mail import send_mail
from django.db import models
from django.contrib.postgres.fields import ArrayField
from toe_hiring_2020.settings import DEFAULT_FROM_EMAIL


# TODO: Put your dog questions model here


def arrayfield_default_value():
    return "NA"


class Pet(models.Model):
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
            message = f'Thank you for taking the time to fill out the form. \n'

            is_walked = form_response.cleaned_data['daily_walk']
            if is_walked:
                message += f'Your dog loves the walks! Trust us. \n'
            else:
                message += f'Hope you have a fenced in yard.\n'

            breed = form_response.cleaned_data["breed"]
            if len(breed) != 0 or breed.isspace():
                message += f'{breed}s are so cute!!\n'

            age = form_response.cleaned_data['age']
            age_message = f'{age} years old. '
            if age < 2:
                age_message += f'Still a puppy. \n'
            elif age > 9:
                age_message += f'An old friend. \n'
            else:
                age_message += f'Prime of their life! \n'
            message += age_message

            trick = form_response.cleaned_data['trick']
            trick_message = 'Tricks: \n'
            is_none = re.search('\bNone', trick[0])

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

        #             f'{tricks if len(tricks)==1 else [i for i in tricks]}'
        send_mail(subject, email_message(self), DEFAULT_FROM_EMAIL,
                  [self.cleaned_data['email'], 'admin@dogstartup.com'],
                  fail_silently=False)
