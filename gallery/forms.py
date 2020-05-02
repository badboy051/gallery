from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={}))
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')