from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet, formset_factory

from .models import *


# TODO: Put your dog questions form here
class DogForm(forms.ModelForm):
    class Meta:
        model = DogOwner
        exclude = ['owner']
        labels = {
            'email': 'Please provide an Email address to receive results.',
            'tricks': 'What tricks does your dog know? Select all that apply:',
            'age': 'How old is your dog?',
            'breed': 'What is the breed of your dog?',
            'daily_walk': 'Do you walk your dog daily?'
        }


PetFormset = inlineformset_factory(DogOwner, Pet, form=DogForm, extra=1)

#
# class BasePetFormset(BaseInlineFormSet):
#     def add_fields(self, form, index):
#         super(BasePetFormset, self).add_fields(form, index)
#
#         form.nested = PetFormset(
#             instance=form.instance,
#             data=form.data if form.is_bound else None,
#             files=form.files if form.is_bound else None,
#             prefix='pet-%s-%s' % (form.prefix, PetFormset.get_default_prefix())
#         )
#
#     def is_valid(self):
#         result = super(BasePetFormset, self).is_valid()
#
#         if self.is_bound:
#             for form in self.forms:
#                 if hasattr(form, 'nested'):
#                     result = result and form.nested.is_valid()
#
#         return result
#
#     def save(self, commit=True):
#
#         result = super(BasePetFormset, self).save(commit=commit)
#
#         for form in self.forms:
#             if hasattr(form, 'nested'):
#                 if not self._should_delete_form(form):
#                     form.nested.save(commit=commit)
#
#         return result




# daily_walk = forms.BooleanField(, required=False)
# dog_breed = forms.CharField(
#     ,
#     max_length=40,
#     empty_value='',
#     strip=True
# )
# dog_age = forms.IntegerField(label='How old is your dog?', max_value=30)
# dog_tricks = forms.ModelMultipleChoiceField(
#     ,
#     widget=forms.CheckboxSelectMultiple,
#     queryset=Trick.tricks.all().order_by('name'),
#     required=False
# )
# user_email = forms.CharField(
#     label='Please provide an Email address to receive results.',
#     max_length=50,
#     required=True
# )
