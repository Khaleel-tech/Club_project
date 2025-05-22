from django.db import models

class EventRegistration(models.Model):
    event = models.ForeignKey('ClubIncharge.Event', on_delete=models.CASCADE, related_name='registrations')
    student = models.ForeignKey('SuperAdmin.Student', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ['event', 'student']

    def __str__(self):
        return f"{self.student.name} - {self.event.title}"
