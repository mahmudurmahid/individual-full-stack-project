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
    address = models.TextField()
    date = models.DateTimeField()
    music_genre = models.CharField(max_length=50, choices=MUSIC_GENRES)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events")  # Organizer (event holder)

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
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    venue_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.role == 'customer':
            return f"{self.first_name} {self.last_name} - {self.role}"
        elif self.role == 'event_holder':
            return f"{self.venue_name} - {self.role}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
