from django.contrib import admin
from .models import Event, Booking

# Customize the Event model in the admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'address', 'date', 'music_genre', 'created_by')  # Columns to display
    list_filter = ('music_genre', 'date')  # Filters on the right
    search_fields = ('title', 'venue', 'address', 'music_genre')  # Search bar
    ordering = ('date',)  # Order by date by default

# Customize the Booking model in the admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'ticket_count', 'booked_on')  # Columns to display
    list_filter = ('event', 'booked_on')  # Filters on the right
    search_fields = ('user__username', 'event__title')  # Search bar for user and event
    date_hierarchy = 'booked_on'  # Date drill-down navigation
