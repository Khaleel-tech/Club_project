from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils import timezone
from SuperAdmin.models import Student

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    event_incharge = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_events',
        limit_choices_to={'role': 'Club Incharge'}
    )
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    registration_deadline = models.DateTimeField(null=True, blank=True)
    event_poster = models.ImageField(upload_to='event_posters/', null=True, blank=True)
    max_participants = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def is_registration_open(self):
        now = timezone.now()
        if not self.registration_deadline:
            return False
        return now <= self.registration_deadline

    def get_registration_status(self):
        if not self.registration_deadline:
            return "Registration deadline not set"
        
        now = timezone.now()
        if now > self.registration_deadline:
            return "Registration closed"
        elif self.max_participants > 0 and self.participant_count() >= self.max_participants:
            return "Event is full"
        else:
            return "Registration open"

    def participant_count(self):
        return self.registrations.count()

    def get_available_spots(self):
        if self.max_participants == 0:
            return "Unlimited"
        registered = self.participant_count()
        remaining = self.max_participants - registered
        return remaining if remaining >= 0 else 0

@receiver(pre_delete, sender=Event)
def delete_event_files(sender, instance, **kwargs):
    """Delete files when event is deleted"""
    if instance.event_poster:
        instance.event_poster.delete(False)
