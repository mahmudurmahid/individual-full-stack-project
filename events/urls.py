from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),  # Static homepage
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Custom login view
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout page
    path('events/', views.event_list, name='event_list'),  # Upcoming events (customers only)
    path('create/', views.create_event, name='create_event'),  # Create an event (event holders only)
    path('my-events/', views.my_events, name='my_events'),  # Event holder's created events
    path('book/<int:event_id>/', views.book_event, name='book_event'),  # Book an event (customers only)
    path('my-bookings/', views.booked_events, name='booked_events'),  # Customer's booked events
]
