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
    existing_booking = Booking.objects.filter(user=request.user, event=event).first()
    if existing_booking:
        print(f"User {request.user.username} already booked the event: {event.title}")
        return redirect('my_bookings')  # Redirect if already booked

    # Create a booking
    booking = Booking.objects.create(user=request.user, event=event)
    print(f"Booking created: {booking}")
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
            event.organizer = request.user  # Assign the current user as the organizer
            event.save()
            print(f"Event '{event.title}' created successfully by {event.organizer}.")
            return redirect('my_events')
        else:
            print("Form errors:", form.errors)  # Log form errors
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


@login_required
def my_events(request):
    """View to display events created by the logged-in event holder."""
    # Fetch events created by the logged-in organizer
    events = Event.objects.filter(organizer=request.user)
    print(f"Events created by {request.user.username}: {events.count()}")  # Debugging info

    return render(request, 'my_events.html', {'my_events': events})


@login_required
def event_list(request):
    """View to display all available events."""
    events = Event.objects.all()  # Fetch all events without filtering by user
    print(f"Total events fetched: {events.count()}")  # Debugging info
    return render(request, 'event_list.html', {'events': events})


@login_required
def my_bookings(request):
    """View to display all bookings made by the logged-in user."""
    bookings = Booking.objects.filter(user=request.user)
    print(f"Bookings for user {request.user.username}: {bookings.count()}")  # Debugging info
    return render(request, 'booked_events.html', {'bookings': bookings})
