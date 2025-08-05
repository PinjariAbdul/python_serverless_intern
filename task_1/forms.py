from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'profile_picture', 'username', 'email',
                  'password1', 'password2', 'user_type', 'address_line1', 'city', 'state', 'pincode']

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get("password1")
        confirm_pwd = cleaned_data.get("password2")
        if pwd != confirm_pwd:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
