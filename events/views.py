from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EventForm, CustomLoginForm
from .models import Event, Booking


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.profile.role == 'customer':
                return redirect('customer_home')  # Redirect for customers
            elif user.profile.role == 'event_holder':
                return redirect('event_holder_home')  # Redirect for event holders
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                if user.profile.role == 'customer':
                    return redirect('customer_home')
                elif user.profile.role == 'event_holder':
                    return redirect('event_holder_home')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def customer_home(request):
    return render(request, 'customer_home.html')


@login_required
def event_holder_home(request):
    return render(request, 'event_holder_home.html')


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('my_events')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
def my_events(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'my_events.html', {'events': events})


@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booked_events.html', {'bookings': bookings})
