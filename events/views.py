from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, EventForm, CustomLoginForm
from .models import Event, Booking


# Homepage View
class HomePage(TemplateView):
    """
    Displays static homepage
    """
    template_name = 'index.html'


# Event Listing View (Customers Only)
@login_required
def event_list(request):
    if request.user.profile.role != 'customer':
        return HttpResponseForbidden("Only customers can view all upcoming events.")
    
    events = Event.objects.all()

    # Apply filters if criteria are provided
    music_genre = request.GET.get('music_genre')
    city = request.GET.get('city')
    date = request.GET.get('date')

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
            backend_path = 'django.contrib.auth.backends.ModelBackend'  # Specify the backend explicitly
            login(request, user, backend=backend_path)
            return redirect('home')
        else:
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
        return HttpResponseForbidden("Only event holders can create events.")

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('my_events')  # Redirect to the event holder's events
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})


# Event Holder's Created Events (Event Holders Only)
@login_required
def my_events(request):
    if request.user.profile.role != 'event_holder':
        return HttpResponseForbidden("Only event holders can view their created events.")

    events = Event.objects.filter(created_by=request.user)
    return render(request, 'my_events.html', {'events': events})


# Ticket Booking View (Customers Only)
@login_required
def book_event(request, event_id):
    if request.user.profile.role != 'customer':
        return HttpResponseForbidden("Only customers can book tickets.")
    
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        ticket_count = int(request.POST.get('ticket_count', 1))
        if ticket_count < 1 or ticket_count > 5:
            return HttpResponseBadRequest("You can only book between 1 and 5 tickets.")
        
        booking, created = Booking.objects.get_or_create(user=request.user, event=event)
        booking.ticket_count = ticket_count
        booking.save()

        return render(request, 'booking_confirmed.html', {'event': event, 'ticket_count': ticket_count})

    return render(request, 'book_event.html', {'event': event})


# Booking Listing View (Customers Only)
@login_required
def booked_events(request):
    if request.user.profile.role != 'customer':
        return HttpResponseForbidden("Only customers can view their bookings.")
    
    bookings = Booking.objects.filter(user=request.user).select_related('event')
    return render(request, 'booked_events.html', {'bookings': bookings})
