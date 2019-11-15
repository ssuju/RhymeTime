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

    class Meta:
        model = User
        fields = {'email', 'first_name', 'last_name'}




class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

