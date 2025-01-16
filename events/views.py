from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EventForm
from .models import Event

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'event_list.html', {'events': events})

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