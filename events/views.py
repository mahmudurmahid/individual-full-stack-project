from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import RegisterForm, EventForm
from .models import Event, Booking, Profile

# Create your views here
# Homepage View
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'index.html'

# Event Listing View
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'event_list.html', {'events': events})

# User Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Event Creation View (Event Holders Only)
@login_required
def create_event(request):
    # Ensure user has a profile
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    # Only event holders can create events
    if request.user.profile.role != 'event_holder':
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
    event = get_object_or_404(Event, id=event_id)
    
    # Prevent duplicate bookings
    if Booking.objects.filter(user=request.user, event=event).exists():
        return render(request, 'booking_confirmed.html', {'event': event, 'message': 'You have already booked this event.'})

    Booking.objects.create(user=request.user, event=event)
    return render(request, 'booking_confirmed.html', {'event': event, 'message': 'Your booking was successful!'})
