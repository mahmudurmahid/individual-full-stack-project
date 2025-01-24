from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Event, Profile
import re


class RegisterForm(UserCreationForm):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('event_holder', 'Event Holder'),
    )
    email = forms.EmailField()
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.create(
                user=user,
                role=self.cleaned_data['role']
            )
        return user


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No account found with this email.")

        user = authenticate(username=email, password=password)
        if not user:
            raise forms.ValidationError("Invalid credentials. Please try again.")
        return cleaned_data


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'bio', 'venue', 'address', 'date', 'music_genre']

    def clean_address(self):
        address = self.cleaned_data.get('address')
        pattern = r'^\d+\s[\w\s]+,\s[\w\s]+,\s[A-Z]{1,2}\d{1,2}\s?\d[A-Z]{2}$'
        if not re.match(pattern, address):
            raise forms.ValidationError(
                "Please enter a valid address in the format: '123 Street Name, City, AB1 2CD'"
            )
        return address
