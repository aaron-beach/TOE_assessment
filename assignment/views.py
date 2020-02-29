from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import *
from django.views import View
from assignment.forms import *
from django.core.mail import send_mail, BadHeaderError

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
            is_walked = form.cleaned_data['daily_walk']
            breed = form.cleaned_data['breed']
            age = form.cleaned_data['age']
            tricks = form.cleaned_data['trick']
            print(tricks)
            try:
                send_mail(
                    'Thank you!',
                    f'Thank you for taking the time to fill out the form. \n'
                    f'{"Your dog loves the walks! Trust us. " if is_walked else "Hope you have a fenced in yard."}\n'
                    f'{breed} is so cute!!\n'
                    f'{age}{" years old. Still a puppy. " if age < 2 else " years old. An old friend. "}\n'
                    f'{tricks if len(tricks)==1 else [i for i in tricks]}',

                    DEFAULT_FROM_EMAIL,
                    [email_contact],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponseRedirect(self.get_success_url())
        else:
            print(form.errors.as_json())
            messages.error(request, "Error")
        return render(request, 'success.html', {'form': form})


class Success(TemplateView):
    template_name = 'success.html'
