from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('customer-home/', views.customer_home, name='customer_home'),
    path('event-holder-home/', views.event_holder_home, name='event_holder_home'),
    path('events/', views.event_list, name='event_list'),
    path('my-events/', views.my_events, name='my_events'),
    path('create-event/', views.create_event, name='create_event'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('events/book/<int:event_id>/', views.book_event, name='book_event'),
    path('bookings/add-ticket/<int:booking_id>/', views.add_ticket, name='add_ticket'),
    path('bookings/remove-ticket/<int:booking_id>/', views.remove_ticket, name='remove_ticket'),
]
