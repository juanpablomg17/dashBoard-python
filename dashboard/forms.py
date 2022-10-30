from django import forms
from .models import Death


class ProductForm(forms.ModelForm):
    class Meta:
        model = Death
        fields = '__all__'

