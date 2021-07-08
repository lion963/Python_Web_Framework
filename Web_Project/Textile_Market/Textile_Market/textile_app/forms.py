from django import forms
from django.contrib.auth.models import User

from Textile_Market.textile_app.models import AddOffer, Profile


class OfferForm(forms.ModelForm):
    class Meta:
        model = AddOffer
        fields = "__all__"

        widgets = {
            'garment_type': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'})
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs= {'class': 'form-control'}),
            'password': forms.PasswordInput(attrs= {'class': 'form-control'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'company', 'telephone', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input'})
        }

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
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password',
            }
        )
    )
