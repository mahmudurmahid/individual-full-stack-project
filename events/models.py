from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Event(models.Model):
    MUSIC_GENRES = [
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('hip_hop', 'Hip-Hop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('electronic', 'Electronic'),
        ('country', 'Country'),
        ('reggae', 'Reggae'),
    ]

    title = models.CharField(max_length=200)
    bio = models.TextField()
    venue = models.CharField(max_length=200)
    street = models.CharField(max_length=200)  # New field for street
    city = models.CharField(max_length=100)  # New field for city
    postcode = models.CharField(max_length=20)  # New field for postcode
    date = models.DateTimeField()
    music_genre = models.CharField(max_length=50, choices=MUSIC_GENRES)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events")

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)
    ticket_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.event.title} ({self.ticket_count} tickets)"


class Profile(models.Model):
    USER_ROLES = (
        ('customer', 'Customer'),
        ('event_holder', 'Event Holder'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='customer')
    venue_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
