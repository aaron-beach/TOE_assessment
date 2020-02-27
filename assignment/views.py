from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.views import View
from assignment.models import *
from assignment.forms import *
from django.core.mail import send_mail


class Index(FormView):
    template_name = "index.html"

    form_class = DogForm
    success_url = '/success/'

    def get_context_data(self, **kwargs):
        form = self.form_class(initial=self.initial)
        context = super(Index, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        print("posted")
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        pet_form = PetFormset(self.request.POST)

        # TODO: Process form data here by saving to DB and sending Email

        if form.is_valid() and pet_form.is_valid():
            self.object = form.save()
            pet_form.instance = self.object
            pet_form.save()

            """
            Email results to DogOwner
            """
            message = form.cleaned_data['message']
            sender = ['results@dogstartup.com']
            recipients = form.cleaned_data['user_email']

            send_mail(message, sender, recipients, subject='Dog Startup Results')

            return HttpResponseRedirect(self.get_success_url())


class Success(TemplateView):
    template_name = 'success.html'
