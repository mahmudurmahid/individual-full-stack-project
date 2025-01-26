from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EventForm, CustomLoginForm
from .models import Event, Booking


def index(request):
    """Landing page view."""
    return render(request, 'index.html')


def register(request):
    """User registration view."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect based on user role
            if hasattr(user, 'profile') and user.profile.role == 'customer':
                return redirect('customer_home')
            elif hasattr(user, 'profile') and user.profile.role == 'event_holder':
                return redirect('event_holder_home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    """User login view."""
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                # Redirect based on user role
                if hasattr(user, 'profile') and user.profile.role == 'customer':
                    return redirect('customer_home')
                elif hasattr(user, 'profile') and user.profile.role == 'event_holder':
                    return redirect('event_holder_home')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def book_event(request, event_id):
    """View to handle event booking."""
    event = get_object_or_404(Event, id=event_id)

    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated

    # Check if the user has already booked this event
    if Booking.objects.filter(user=request.user, event=event).exists():
        return redirect('my_bookings')  # Redirect if already booked

    # Create a booking
    Booking.objects.create(user=request.user, event=event)
    return redirect('my_bookings')


@login_required
def logout_view(request):
    """User logout view."""
    logout(request)
    return redirect('login')


@login_required
def customer_home(request):
    """Home page for customers."""
    return render(request, 'customer_home.html')


@login_required
def event_holder_home(request):
    """Home page for event holders."""
    return render(request, 'event_holder_home.html')


@login_required
def create_event(request):
    """View to create a new event."""
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
    """View to display events created by the logged-in event holder."""
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'my_events.html', {'events': events})


@login_required
def event_list(request):
    """View to display all available events."""
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


@login_required
def my_bookings(request):
    """View to display all bookings made by the logged-in user."""
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booked_events.html', {'bookings': bookings})
