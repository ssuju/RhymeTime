from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


now = timezone.now()


def home(request):
    return render(request, 'rhymesapp/home.html',
                 {'rhymesapp': home})

@login_required
def audio_list(request):
    return render(request, 'rhymesapp/audio_list.html',
                 {'rhymesapp': audio_list})


@login_required
def account_information(request):
#    account = Account.objects.filter(created_date__lte=timezone.now())
    account = Account.objects.all()
    return render(request, 'rhymesapp/account_information.html',
                 {'accounts': account})


def register(request):
    return render(request, 'rhymesapp/register.html', {'rhymesapp': register})


def nurseryList(request):
    return render(request, 'rhymesapp/nurseryList.html', {'rhymesapp': nurseryList})


def nurseryPage(request):
    return render(request, 'rhymesapp/nurseryPage.html', {'rhymesapp': nurseryPage})


@login_required
def upgrade(request):
    return render(request, 'rhymesapp/upgrade.html', {'rhymesapp': upgrade})


def account_created(request):
    return render(request, 'rhymesapp/account_created.html', {'rhymesapp': account_created})


def email(request):
    return render(request, 'rhymesapp/contact.html', {'rhymesapp': email})


def success(request):
    return render(request, 'rhymesapp/success.html', {'rhymesapp': success})


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'rhymesapp/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.street_address = form.cleaned_data['street_address']
                user.save()
                # save the same info to account

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                phone_number = form.cleaned_data['phone_number']
                street_address = form.cleaned_data['street_address']
              #  account.first_name = form.cleaned_data['phone']
                email = form.cleaned_data['email']
               # account.first_name = form.cleaned_data['street_address']
                account = Account(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                                  street_address=street_address)
                account.save()

                # Login the user
                login(request, user)

                # redirect to accounts_created page:
                return HttpResponseRedirect('/register/account_created/')

    # No post data avaliable, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/email/success/')
    return render(request, 'rhymesapp/contact.html', {'form': form})