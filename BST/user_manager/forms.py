from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label = u'Username', max_length = 30)
    email = forms.EmailField(label = u'Email')
    password1 = forms.CharField(
        label = u'Password',
        widget = forms.PasswordInput()
    )

    password2 = forms.CharField(
        label = u'Repeat Password',
        widget = forms.PasswordInput()
    )

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Los passwords no coinciden')       

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('El nombre de usuario solo puede contener'
            'caracteres alphanumericos y underscore')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya usado')

    def clean_email(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email ya usado')
