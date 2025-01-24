from django.contrib import admin
from .models import Event, Booking, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Inline Profile admin to include Profile fields in User admin
class ProfileInline(admin.StackedInline):
    model = Profile  # Link the Profile model to the User model
    can_delete = False  # Prevent deletion of Profile from this view
    verbose_name_plural = 'Profile Details'  # Label the section
    fk_name = 'user'  # Specify the foreign key linking User to Profile


# Custom User admin to show Profile details
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)  # Add ProfileInline to User admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role')  # Add the role column
    list_select_related = ('profile',)  # Optimize queries with related Profile fields

    def get_role(self, instance):
        return instance.profile.role  # Display the role (customer/event_holder) from Profile
    get_role.short_description = 'Role'  # Rename the column header
    get_role.admin_order_field = 'profile__role'  # Allow sorting by role


# Unregister the default User admin
admin.site.unregister(User)
# Register the custom User admin
admin.site.register(User, CustomUserAdmin)


# Event admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'venue', 'address', 'date', 'music_genre', 'created_by')  # Columns to display
    list_filter = ('music_genre', 'date')  # Filters on the right
    search_fields = ('title', 'venue', 'address', 'music_genre', 'created_by__username')  # Search bar
    ordering = ('date',)  # Order by date by default


# Booking admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'ticket_count', 'booked_on')  # Columns to display
    list_filter = ('event', 'booked_on')  # Filters on the right
    search_fields = ('user__username', 'event__title')  # Search bar for user and event
    date_hierarchy = 'booked_on'  # Date drill-down navigation
