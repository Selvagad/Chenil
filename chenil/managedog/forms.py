from django import forms
from .models import Dog

class DogModelForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ["name","num_id","dog_master"]