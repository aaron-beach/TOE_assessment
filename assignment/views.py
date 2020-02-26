from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.views import View
from assignment.models import *
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
            return HttpResponseRedirect(self.get_success_url())


class Success(TemplateView):
    template_name = 'success.html'
