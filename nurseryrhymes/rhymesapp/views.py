from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .forms import EditProfileForm
from django.conf import settings


now = timezone.now()


def home(request):
    return render(request, 'rhymesapp/home.html',
                 {'rhymesapp': home})


#@login_required
def audio_list(request):
    return render(request, 'rhymesapp/audio_list.html',
                 {'rhymesapp': audio_list})


@login_required
def account_information(request):
    account = Account.objects.filter(created_date__lte=timezone.now())
    return render(request, 'rhymesapp/account_information.html',
                 {'accounts': account})


def register(request):
    return render(request, 'rhymesapp/register.html', {'rhymesapp': register})


def nurseryList(request):
    return render(request, 'rhymesapp/nurseryList.html', {'rhymesapp': nurseryList})


def nurseryPage(request):
    return render(request, 'rhymesapp/nurseryPage.html', {'rhymesapp': nurseryPage})

def londonBridge(request):
    return render(request, 'rhymesapp/londonBridge.html', {'rhymesapp': londonBridge})

def littleStar(request):
    return render(request, 'rhymesapp/littleStar.html', {'rhymesapp': littleStar})

def jackJill(request):
    return render(request, 'rhymesapp/jackJill.html', {'rhymesapp': jackJill})

def itsySpider(request):
    return render(request, 'rhymesapp/itsySpider.html', {'rhymesapp': itsySpider})

def humptyDumpty(request):
    return render(request, 'rhymesapp/humptyDumpty.html', {'rhymesapp': humptyDumpty})

def hickoryDock(request):
    return render(request, 'rhymesapp/hickoryDock.html', {'rhymesapp': humptyDumpty})


#@login_required
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
                user.save()

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
            message = form.cleaned_data['message']
            email_address = form.cleaned_data['email_address']
            recipient_list = ['teamthreenurseryrhymes@gmail.com', ]
            try:
                send_mail(subject, message, email_address, recipient_list, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/email/success/')
    return render(request, 'rhymesapp/contact.html', {'form': form})


def infoView(request):
    args = {'user': request.user}
    return render(request, 'rhymesapp/account_information.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('/account_information')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'rhymesapp/edit_profile.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account_information')
        else:
            return redirect('/change_password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'rhymesapp/change_password.html', args)



