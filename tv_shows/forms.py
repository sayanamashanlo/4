from django import  forms
from . import models

# форма поля-->логика

class ShowForm(forms.ModelForm):
    class Meta:
        model = models.Show
        fields = '__all__'
        