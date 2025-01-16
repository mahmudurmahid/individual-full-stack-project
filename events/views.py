from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EventForm
from .models import Event, Booking


# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'event_list.html', {'events': events})

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

@login_required
def create_event(request):
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

from django.shortcuts import get_object_or_404

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    Booking.objects.create(user=request.user, event=event)
    return render(request, 'booking_confirmed.html', {'event': event})
