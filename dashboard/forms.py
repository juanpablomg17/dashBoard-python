from django import forms
from .models import Death, Birth, Education


class ProductForm(forms.ModelForm):
    class Meta:
        model = Death
        fields = '__all__'
        
        
class BirthForm(forms.ModelForm):
    class Meta:
        model = Birth
        fields = '__all__'
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

