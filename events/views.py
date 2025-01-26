from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, EventForm, CustomLoginForm  # Added CustomLoginForm
from .models import Event, Booking


def index(request):
    return render(request, 'index.html')


def event_list(request):
    music_genre = request.GET.get('music_genre', '')
    city = request.GET.get('city', '')
    date = request.GET.get('date', '')

    events = Event.objects.all()
    if music_genre:
        events = events.filter(music_genre=music_genre)
    if city:
        events = events.filter(address__icontains=city)
    if date:
        events = events.filter(date__date=date)

    genres = Event.objects.values_list('music_genre', flat=True).distinct()
    cities = Event.objects.values_list('address', flat=True).distinct()
    return render(request, 'event_list.html', {
        'events': events,
        'genres': genres,
        'cities': cities,
    })


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booked_events.html', {'bookings': bookings})


@login_required
def my_events(request):
    my_events = Event.objects.filter(organizer=request.user)
    return render(request, 'my_events.html', {'my_events': my_events})


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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        ticket_count = int(request.POST.get('ticket_count', 1))
        Booking.objects.create(user=request.user, event=event, ticket_count=ticket_count)
        return redirect('my_bookings')
    return render(request, 'book_event.html', {'event': event})
