from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import *
from django.views import View
from .models import Pet
from assignment.forms import *


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
            Pet.email_user(form)
            # try:
            #
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')

            return HttpResponseRedirect(self.get_success_url())
        else:
            print(form.errors.as_json())
            messages.error(request, "Error")
        return render(request, 'success.html', {'form': form})


class Success(TemplateView):
    template_name = 'success.html'
