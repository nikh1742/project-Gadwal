from django import forms
from django.forms import ClearableFileInput
from .models import CollectionModel, SareeModel,CustomerContactModel

class CollectionForm(forms.ModelForm):
    """Model form created from CollectionModel."""
    class Meta:
        model = CollectionModel
        fields = ['collection_name',]

class SareeModelForm(forms.ModelForm):
    """Model form created from SareeModel"""
    class Meta:
        model = SareeModel
        fields = ['saree_img',
        #  'collection_name'
         ]
        widgets = {
            'saree_img': ClearableFileInput(attrs={'multiple':True}),
        }

class CustomerContactForm(forms.ModelForm):
    """Model form created from CustomerContactModel"""
    class Meta:
        model = CustomerContactModel
        fields = '__all__'