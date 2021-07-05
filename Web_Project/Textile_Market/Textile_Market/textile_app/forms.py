from django import forms

from Textile_Market.textile_app.models import AddOffer


class AddOfferForm(forms.ModelForm):
    class Meta:
        model = AddOffer
        fields = "__all__"

        widgets = {
            'garment_type': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'})
        }
