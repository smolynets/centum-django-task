from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'profile_image'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Hash the password
        if commit:
            user.save()
        return user
