from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.views import View
from assignment.forms import *
from django.core.mail import EmailMessage, send_mail

from toe_hiring_2020.settings import DEFAULT_FROM_EMAIL


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
            email_contact = form.cleaned_data['email']
            print(email_contact)
            send_mail(
                'Thank you!',
                'Here is the message.',
                DEFAULT_FROM_EMAIL,
                [email_contact],
                fail_silently=False,
            )
            return HttpResponseRedirect(self.get_success_url())
        else:
            print(form.errors.as_json())
            messages.error(request, "Error")
        return render(request, 'success.html', {'form': form})


class Success(TemplateView):
    template_name = 'success.html'
