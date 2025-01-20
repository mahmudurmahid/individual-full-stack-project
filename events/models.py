from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    booked_on = models.DateTimeField(auto_now_add=True)
    ticket_count = models.PositiveIntegerField(default=1)  # Default is 1 ticket

    def __str__(self):
        return f"{self.user.username} - {self.event.title} ({self.ticket_count} tickets)"

class Profile(models.Model):
    USER_ROLES = (
        ('customer', 'Customer'),
        ('event_holder', 'Event Holder'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='customer')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()