from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),  # static homepage
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Use CustomLoginView
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Correct import here
    path('events/', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    path('book/<int:event_id>/', views.book_event, name='book_event'),
    path('my-bookings/', views.booked_events, name='booked_events'),
]