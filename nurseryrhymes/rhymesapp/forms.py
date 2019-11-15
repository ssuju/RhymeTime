from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import User
from .models import Account
from django import forms


class AccountForm(forms.ModelForm):
   class Meta:
       model = Account
       fields = ('first_name', 'last_name', 'phone', 'email', 'zipcode')


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email'}


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150)
    email_address = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

