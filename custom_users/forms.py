from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER_TYPE = (
    ("MALE", "M"),
    ("FEMALE", 'Ж')
)


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label='Укажите номер телефона')
    birthday = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    # логика для отображения полей
    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'birthday',
            'gender'
        )


    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


    # widget=forms.
