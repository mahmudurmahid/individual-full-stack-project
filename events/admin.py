from django.contrib import admin
from .models import Event, Booking, Profile

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'city', 'date', 'music_genre', 'organizer')
    search_fields = ('title', 'venue', 'city', 'music_genre', 'organizer__username')
    list_filter = ('music_genre', 'city', 'date')
    ordering = ('-date',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'booked_on', 'ticket_count')
    search_fields = ('user__username', 'event__title')
    list_filter = ('booked_on',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'first_name', 'last_name', 'venue_name')
    search_fields = ('user__username', 'role', 'first_name', 'last_name', 'venue_name')
    list_filter = ('role',)

admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Profile, ProfileAdmin)
