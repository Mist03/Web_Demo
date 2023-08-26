from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class LoginForm(forms.Form):
#   username = forms.CharField(max_length=65)
#    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100, initial=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
