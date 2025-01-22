from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event, Profile
import re

class RegisterForm(UserCreationForm):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('event_holder', 'Event Holder'),
    )
    email = forms.EmailField()
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    venue_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'venue_name', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.get(user=user)
            profile.role = self.cleaned_data['role']
            profile.save()
        return user

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'bio', 'venue', 'address', 'date', 'music_genre']

    def clean_address(self):
        address = self.cleaned_data.get('address')
        # Define a regex pattern for validating UK-style addresses
        pattern = r'^\d+\s\w+(?:\s\w+)*\s\w+(?:\s\w+)*\s[A-Z]{1,2}\d{1,2}\s?\d[A-Z]{2}$'
        
        if not re.match(pattern, address):
            raise forms.ValidationError(
                "Please enter a valid address in the format: '3 Abbey Road London NW8 9AY'"
            )
        
        return address

