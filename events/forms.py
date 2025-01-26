from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Event, Profile


class RegisterForm(UserCreationForm):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('event_holder', 'Event Holder'),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        }),
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Select your role'
        }),
    )
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        }),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'role']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm your password'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class CustomLoginForm(forms.Form):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password'
    }))

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid email or password.")
        return self.cleaned_data


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'bio', 'venue', 'street', 'city', 'postcode', 'date', 'music_genre']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the event title'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter a short bio or description of the event'
            }),
            'venue': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the venue name'
            }),
            'street': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the street address'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the city'
            }),
            'postcode': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the postcode'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Select the event date and time'
            }),
            'music_genre': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Select a music genre'
            }),
        }
