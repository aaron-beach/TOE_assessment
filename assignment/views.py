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
        form = self.get_form()

        # Checking form for errors
        if form.is_valid():
        # Save the validated form to the DB
            form.save()

        # After saving email user unless badheader is provided.    
            try:
                Pet.email_user(form)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponseRedirect(self.get_success_url())
        else:
        # Print any invalid errors to the console    
            print(form.errors.as_json())
        return render(request, 'success.html', {'form': form})


class Success(TemplateView):
    template_name = 'success.html'
