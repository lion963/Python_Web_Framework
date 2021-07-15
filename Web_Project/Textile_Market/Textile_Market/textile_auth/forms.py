from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from Textile_Market.textile_profile.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter username',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password',
            }
        )
    )

    def clean(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError('Email and/or password incorrect')


class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'type', 'telephone']
        widgets = {
            'type': forms.Select(attrs= {'class': 'form-control'})
        }

