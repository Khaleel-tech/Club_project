from django import forms
from .models import Event
from SuperAdmin.models import Student

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 
            'description', 
            'event_incharge',
            'start_date', 
            'end_date', 
            'location', 
            'max_participants', 
            'registration_deadline', 
            'event_poster'
        ]
        widgets = {
            'event_incharge': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'start_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'end_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'registration_deadline': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'rows': 4, 'class': 'form-control'}
            ),
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter event title'}
            ),
            'location': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter event location'}
            ),
            'max_participants': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': '0 for unlimited'}
            ),
            'event_poster': forms.FileInput(
                attrs={'class': 'form-control'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show Club Incharges in the dropdown
        club_incharges = Student.objects.filter(role='Club Incharge')
        self.fields['event_incharge'].queryset = club_incharges
        self.fields['event_incharge'].label_from_instance = lambda obj: f"{obj.name} ({obj.username})"

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        registration_deadline = cleaned_data.get('registration_deadline')
        event_incharge = cleaned_data.get('event_incharge')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("End date must be after start date")

        if registration_deadline and start_date and registration_deadline > start_date:
            raise forms.ValidationError("Registration deadline must be before event start date")

        if event_incharge and event_incharge.role != 'Club Incharge':
            raise forms.ValidationError("Event incharge must be a Club Incharge")

        return cleaned_data
