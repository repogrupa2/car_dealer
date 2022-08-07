from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Branch, BranchCarAvailability

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
        fields = ('address', 'city', 'open_from', 'open_till', 'mail', 'mobile', 'remarks')


class BranchCarAvailabilityCreate(forms.ModelForm):
    class Meta:
        model = BranchCarAvailability
        fields = ('branch_id', 'vehicle_id', 'availability')
