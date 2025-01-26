from django.contrib import admin
from .models import Event, Booking, Profile

# Event Admin
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'street', 'city', 'postcode', 'date', 'music_genre', 'organizer')
    search_fields = ('title', 'venue', 'street', 'city', 'postcode', 'music_genre', 'organizer__username')
    list_filter = ('music_genre', 'city', 'date')
    ordering = ('-date',)
    fieldsets = (
        ('Event Details', {
            'fields': ('title', 'bio', 'music_genre', 'organizer')
        }),
        ('Location', {
            'fields': ('venue', 'street', 'city', 'postcode')
        }),
        ('Date and Time', {
            'fields': ('date',)
        }),
    )

# Booking Admin
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'booked_on', 'ticket_count')
    search_fields = ('user__username', 'event__title')
    list_filter = ('booked_on',)

# Profile Admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'get_first_name', 'get_last_name', 'venue_name')
    search_fields = ('user__username', 'role', 'user__first_name', 'user__last_name', 'venue_name')
    list_filter = ('role',)

    # Methods to display related User fields
    @admin.display(description='First Name')
    def get_first_name(self, obj):
        return obj.user.first_name

    @admin.display(description='Last Name')
    def get_last_name(self, obj):
        return obj.user.last_name

# Register models with the admin site
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Profile, ProfileAdmin)
