from django import forms

from Textile_Market.textile_profile.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'type', 'telephone', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'type': forms.Select(attrs= {'class': 'form-control'})

        }