from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_backends
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now, timedelta
from .forms import RegisterForm, EventForm, CustomLoginForm
from .models import Event, Booking

def index(request):
    """Landing page view."""
    if request.user.is_authenticated:
        if hasattr(request.user, 'profile') and request.user.profile.role == 'customer':
            return redirect('customer_home')  # Redirect customers to their homepage
        elif hasattr(request.user, 'profile') and request.user.profile.role == 'event_holder':
            return redirect('event_holder_home')  # Redirect event holders to their homepage
    return render(request, 'index.html')  # Show the landing page for non-logged-in users

def register(request):
    """User registration view."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Explicitly set the backend to avoid ambiguity
            backend = get_backends()[0]  # Use the first available backend
            user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
            login(request, user)
            # Redirect based on user role
            if hasattr(user, 'profile') and user.profile.role == 'customer':
                return redirect('customer_home')
            elif hasattr(user, 'profile') and user.profile.role == 'event_holder':
                return redirect('event_holder_home')
        else:
            # Debugging form errors
            print("Form Errors:", form.errors)
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
                # Handle "Remember Me" functionality
                remember_me = request.POST.get('remember_me')  # Check for "Remember Me"
                if not remember_me:  # If unchecked, session expires when browser closes
                    request.session.set_expiry(0)
                else:  # If checked or not provided, default session duration is used
                    request.session.set_expiry(1209600)  # 2 weeks (in seconds)
                
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
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'my_events.html', {'my_events': events})

@login_required
def event_list(request):
    """View to display all available events."""
    music_genre = request.GET.get('music_genre', '')
    city = request.GET.get('city', '')
    date = request.GET.get('date', '')

    events = Event.objects.all()
    if music_genre:
        events = events.filter(music_genre=music_genre)
    if city:
        events = events.filter(city__icontains=city)
    if date:
        events = events.filter(date__date=date)  # Filter by specific date

    genres = Event.objects.values_list('music_genre', flat=True).distinct()
    cities = Event.objects.values_list('city', flat=True).distinct()

    return render(request, 'event_list.html', {'events': events, 'genres': genres, 'cities': cities})

    # Filter logic
    events = Event.objects.all()
    if music_genre:
        events = events.filter(music_genre=music_genre)
    if city:
        events = events.filter(address__icontains=city)
    if date:
        week_start = now().strptime(date, "%Y-%m-%d")
        week_end = week_start + timedelta(days=7)
        events = events.filter(date__range=[week_start, week_end])

    genres = Event.objects.values_list('music_genre', flat=True).distinct()
    cities = Event.objects.values_list('address', flat=True).distinct()

    return render(request, 'event_list.html', {'events': events, 'genres': genres, 'cities': cities})

@login_required
def my_bookings(request):
    """View to display all bookings made by the logged-in user."""
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booked_events.html', {'bookings': bookings})

@login_required
def add_ticket(request, booking_id):
    """View to add a ticket to an existing booking."""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.ticket_count += 1
    booking.save()
    return redirect('my_bookings')

@login_required
def remove_ticket(request, booking_id):
    """View to remove a ticket from an existing booking."""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.ticket_count > 1:  # Ensure ticket count does not go below 1
        booking.ticket_count -= 1
        booking.save()
    return redirect('my_bookings')