from django import forms

from core.models import User

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        help_texts = {
            'name': None,
            'email': None,
        }