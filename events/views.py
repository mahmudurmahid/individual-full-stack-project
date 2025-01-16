from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from .forms import RegisterForm
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
