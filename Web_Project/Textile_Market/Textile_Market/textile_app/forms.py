from django import forms

from Textile_Market.textile_app.models import AddOffer, Profile


class OfferForm(forms.ModelForm):
    class Meta:
        model = AddOffer
        fields = ['garment_type', 'quantity', 'description', 'image']

        widgets = {
            'garment_type': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'type', 'telephone', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'type': forms.Select(attrs= {'class': 'form-control'})

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

