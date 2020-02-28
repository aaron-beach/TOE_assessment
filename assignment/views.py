from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.views import View
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
        form = self.get_form()

        # TODO: Process form data here by saving to DB and sending Email

        if form.is_valid():
            form.save()
            print("saved")
            """
            Email results to DogOwner
            """
            # message = form.cleaned_data['message']
         #   sender = ['results@dogstartup.com']
         #    recipients = form.cleaned_data['user_email']
         #
         #    send_mail(message, sender, recipients, subject='Dog Startup Results')

            return HttpResponseRedirect(self.get_success_url())
        return render(request, 'Success',  {'form': form})


class Success(TemplateView):
    template_name = 'success.html'
