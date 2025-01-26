from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Event, Profile


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
            # Prevent duplicate profile creation
            Profile.objects.get_or_create(
                user=user,
                defaults={'role': self.cleaned_data['role']}
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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'music_genre': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 10 or ',' not in address:
            raise forms.ValidationError(
                "Please enter a valid address, including street, city, and postcode."
            )
        return address
