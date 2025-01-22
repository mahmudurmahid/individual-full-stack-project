from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, EventForm, CustomLoginForm
from .models import Event, Booking, Profile


# Homepage View
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'


# Event Listing View
def event_list(request):
    events = Event.objects.all()

    # Get filter criteria from query parameters
    music_genre = request.GET.get('music_genre')
    city = request.GET.get('city')
    date = request.GET.get('date')

    # Apply filters if criteria are provided
    if music_genre:
        events = events.filter(music_genre=music_genre)
    if city:
        events = events.filter(address__icontains=city)
    if date:
        events = events.filter(date__date=date)  # Match only the date part

    # Get unique genres and cities for filter dropdowns
    genres = Event.objects.values_list('music_genre', flat=True).distinct()
    cities = Event.objects.values_list('address', flat=True)
    cities = {addr.split(',')[-2].strip() for addr in cities}  # Extract cities from addresses

    return render(request, 'event_list.html', {
        'events': events,
        'genres': genres,
        'cities': sorted(cities),  # Sorted list of cities
    })


# User Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            # Include error messages in the context if form validation fails
            return render(request, 'register.html', {'form': form, 'errors': form.errors})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True
    next_page = '/'


# Event Creation View (Event Holders Only)
@login_required
def create_event(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'event_holder':
        # Ensure only users with the "event_holder" role can create events
        return HttpResponseForbidden("Only event holders can create events.")

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})


# Ticket Booking View
@login_required
def book_event(request, event_id):
    # Retrieve the specific event to book
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        ticket_count = int(request.POST.get('ticket_count', 1))
        if ticket_count < 1 or ticket_count > 5:
            # Restrict ticket booking to between 1 and 5 tickets
            return HttpResponseBadRequest("You can only book between 1 and 5 tickets.")

        booking, created = Booking.objects.get_or_create(user=request.user, event=event)
        booking.ticket_count = ticket_count
        booking.save()

        return render(request, 'booking_confirmed.html', {'event': event, 'ticket_count': ticket_count})

    return render(request, 'book_event.html', {'event': event})


# Booking Listing View
@login_required
def booked_events(request):
    # Retrieve all bookings made by the logged-in user
    bookings = Booking.objects.filter(user=request.user).select_related('event')
    return render(request, 'booked_events.html', {'bookings': bookings})
