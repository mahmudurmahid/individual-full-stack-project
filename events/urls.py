from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),  # Role-based homepage redirect
    path('customer-home/', views.customer_home, name='customer_home'),  # Customer homepage
    path('event-holder-home/', views.event_holder_home, name='event_holder_home'),  # Event holder homepage
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Custom login view
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout page
    path('events/', views.event_list, name='event_list'),  # Upcoming events (customers only)
    path('book/<int:event_id>/', views.book_event, name='book_event'),  # Book an event (customers only)
    path('create/', views.create_event, name='create_event'),  # Create an event (event holders only)
    path('my-bookings/', views.booked_events, name='my_bookings'),  # Customer's bookings
      path('my-events/', views.my_events, name='my_events'),  # Event holder's events
]
