from django import forms

from Textile_Market.textile_app.models import AddOffer


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


