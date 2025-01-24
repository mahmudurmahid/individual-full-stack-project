from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, EventForm, CustomLoginForm
from .models import Event, Booking, Profile


class HomePage(TemplateView):
    """
    Redirects users based on their role or shows the public homepage if not authenticated.
    """
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'index.html')  # Public homepage
        elif hasattr(request.user, 'profile'):
            if request.user.profile.role == 'customer':
                return redirect('customer_home')
            elif request.user.profile.role == 'event_holder':
                return redirect('event_holder_home')
        return HttpResponseForbidden("Invalid role or profile missing.")


@login_required
def customer_home(request):
    """
    Displays the customer-specific homepage with a list of events and bookings.
    """
    if request.user.profile.role != 'customer':
        return HttpResponseForbidden("Only customers can access this page.")

    events = Event.objects.all()
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'customer_home.html', {'events': events, 'bookings': bookings})


@login_required
def event_holder_home(request):
    """
    Displays the event holder-specific homepage with their created events.
    """
    if request.user.profile.role != 'event_holder':
        return HttpResponseForbidden("Only event holders can access this page.")

    my_events = Event.objects.filter(created_by=request.user)
    return render(request, 'event_holder_home.html', {'my_events': my_events})


@login_required
def event_list(request):
    """
    Displays the list of upcoming events (accessible only to customers).
    """
    if request.user.profile.role != 'customer':
        return HttpResponseForbidden("Only customers can view all upcoming events.")

    events = Event.objects.all()
    music_genre = request.GET.get('music_genre')
    city = request.GET.get('city')
    date = request.GET.get('date')

    if music_genre:
        events = events.filter(music_genre=music_genre)
    if city:
        events = events.filter(address__icontains=city)
    if date:
        events = events.filter(date__date=date)

    genres = Event.objects.values_list('music_genre', flat=True).distinct()
    cities = Event.objects.values_list('address', flat=True)
    cities = {addr.split(',')[-2].strip() for addr in cities}

    return render(request, 'event_list.html', {
        'events': events,
        'genres': genres,
        'cities': sorted(cities),
    })


@login_required
def book_event(request, event_id):
    """
    Allows customers to book an event.
    """
    if request.user.profile.role != 'customer':
        return HttpResponseForbidden("Only customers can book events.")

    event = get_object_or_404(Event, id=event_id)
    booking, created = Booking.objects.get_or_create(user=request.user, event=event)
    if created:
        booking.ticket_count = 1  # Default ticket count (can be customized)
        booking.save()
    return redirect('my_bookings')


@login_required
def booked_events(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booked_events.html', {'bookings': bookings})


def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    """
    Custom login view that uses email and password for authentication.
    """
    template_name = 'login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True
    next_page = '/'


@login_required
def create_event(request):
    """
    Allows event holders to create a new event.
    """
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'event_holder':
        return HttpResponseForbidden("Only event holders can create events.")

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('my_events')  # Redirect to "my events" page
        else:
            print(form.errors)  # Debug: Print form errors in the console
    else:
        form = EventForm()

    return render(request, 'create_event.html', {'form': form})


@login_required
def my_events(request):
    """
    Displays the list of events created by the logged-in event holder.
    """
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'event_holder':
        return HttpResponseForbidden("Only event holders can access this page.")

    my_events = Event.objects.filter(created_by=request.user)
    return render(request, 'my_events.html', {'my_events': my_events})