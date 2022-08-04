from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Branch

from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',)


class BranchCreate(forms.ModelForm):

    class Meta:
        model = Branch
        fields = ('address', 'city', 'opening_hours', 'mail','mobile', 'remarks')
