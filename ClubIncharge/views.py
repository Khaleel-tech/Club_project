from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from SuperAdmin.forms import CompleteProfileForm
from .models import Event
from .forms import EventForm
from django.utils import timezone
from SuperAdmin.models import Student  # Changed this import
from django.contrib.auth.models import Group
from Student.models import EventRegistration  # Add this import
from django.core.cache import cache
from django.db.models import Q
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# from SuperAdmin.urls import urlpatterns

# def ClubIncHome(request):
#     if not request.session.get('username'):
#         messages.error(request, "Please login first")
#         return redirect('login')
    
#     try:
#         username = request.session.get('username')
#         student = Student.objects.get(username=username)
        
#         # Get fresh data from database
#         events = Event.objects.all().order_by('-created_at')
        
#         context = {
#             'incharge': student,
#             'events': events,
#             'branch_names': dict(Student.Branch_choices),
#             'year_names': dict(Student.Year_choices),
#             'training_names': dict(Student.Training_Choices)
#         }
        
#         return render(request, 'ClubIncHome.html', context)
#     except Student.DoesNotExist:
#         messages.error(request, "Student not found.")
#         return redirect('login')

def ClubIncHome(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        student = Student.objects.get(username=username)
        
        # Add strict role verification
        if student.role != 'Club Incharge':
            messages.error(request, "Access denied. This portal is only for Club Incharges.")
            return redirect('Student:student_home')
        
        # Get only active events and their registrations
        events = Event.objects.filter(
            Q(end_date__gte=timezone.now()) |  # Future events
            Q(end_date__isnull=True)  # Events without end date
        ).order_by('-created_at')
        
        # Get recent registrations
        recent_registrations = EventRegistration.objects.select_related(
            'event', 'student'
        ).order_by('-registration_date')[:10]
        
        # Debug print
        print(f"Total events found: {events.count()}")
        print(f"Event IDs: {list(events.values_list('id', flat=True))}")
        
        context = {
            'incharge': student,
            'events': events,
            'recent_registrations': recent_registrations,
            'branch_names': dict(Student.Branch_choices),
            'year_names': dict(Student.Year_choices),
            'training_names': dict(Student.Training_Choices)
        }
        
        return render(request, 'ClubIncHome.html', context)
    except Student.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('login')

def is_club_incharge(user):
    try:
        # Check if the student has ClubIncharge role
        student = Student.objects.get(username=user.username)
        return student.role == 'Club Incharge' or user.is_superuser
    except Student.DoesNotExist:
        return False

@login_required
def incharge_dashboard(request):
    try:
        # Get the student details using username
        student = Student.objects.get(username=request.user.username)
        events = Event.objects.all().order_by('-created_at')
        
        context = {
            'incharge': student,
            'events': events,
            'branch_names': dict(Student.Branch_choices),
            'year_names': dict(Student.Year_choices),
            'training_names': dict(Student.Training_Choices)
        }
        return render(request, 'ClubIncHome.html', context)
    except Student.DoesNotExist:
        messages.error(request, "Club Incharge details not found.")
        return redirect('login')

@login_required
def create_event(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
        
    try:
        username = request.session.get('username')
        user = Student.objects.get(username=username)
        
        # Allow both Super Admin and Club Incharge to create events
        if user.role not in ['Super Admin', 'Club Incharge']:
            messages.error(request, "Access denied. Only Super Admins and Club Incharges can create events")
            return redirect('Student:student_home')
        
        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                event = form.save()
                messages.success(request, 'Event created successfully!')
                # Redirect based on role
                if user.role == 'Super Admin':
                    return redirect('SuperAdmin:SuperAdminHome')
                else:
                    return redirect('ClubIncharge:ClubIncHome')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = EventForm(initial={'event_incharge': user})
            
        context = {
            'form': form,
            'user': user
        }
        return render(request, 'create_event.html', context)
        
    except Student.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login')

@login_required
def event_participants(request, event_id):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        incharge = Student.objects.get(username=username)
        
        # Get the event
        event = Event.objects.get(id=event_id)
        
        # Get all registrations for this event
        registrations = EventRegistration.objects.filter(event=event).select_related('student')
        
        # Calculate attendance statistics
        total_registrations = registrations.count()
        present_count = registrations.filter(attended=True).count()
        absent_count = total_registrations - present_count
        
        # Calculate attendance percentage
        attendance_percentage = (present_count / total_registrations * 100) if total_registrations > 0 else 0
        
        context = {
            'event': event,
            'registrations': registrations,
            'incharge': incharge,
            'branch_names': dict(Student.Branch_choices),
            'year_names': dict(Student.Year_choices),
            'total_registrations': total_registrations,
            'present_count': present_count,
            'absent_count': absent_count,
            'attendance_percentage': round(attendance_percentage, 1)
        }
        
        return render(request, 'event_participants.html', context)
        
    except Event.DoesNotExist:
        messages.error(request, "Event not found.")
        return redirect('ClubIncharge:ClubIncHome')
    except Student.DoesNotExist:
        messages.error(request, "Incharge not found.")
        return redirect('login')

# Student views for event registration
@login_required
def student_event_list(request):
    # Get student details
    student = get_object_or_404(Student, user=request.user)
    
    upcoming_events = Event.objects.filter(
        end_date__gte=timezone.now()
    ).order_by('start_date')
    
    registered_events = Event.objects.filter(
        participants__student=request.user
    )
    
    return render(request, 'student_events.html', {
        'upcoming_events': upcoming_events,
        'registered_events': registered_events,
        'student': student
    })

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    student = get_object_or_404(Student, user=request.user)
    
    if not event.is_registration_open():
        messages.error(request, "Registration for this event has closed.")
        return redirect('ClubIncharge:student_event_list')
    
    if event.max_participants > 0 and event.participant_count() >= event.max_participants:
        messages.error(request, "Event is full.")
        return redirect('ClubIncharge:student_event_list')
    
    if not EventRegistration.objects.filter(event=event, student=student).exists():
        EventRegistration.objects.create(
            event=event, 
            student=student,
        )
        messages.success(request, f"Successfully registered for {event.title}")
    else:
        messages.warning(request, "You are already registered for this event.")
    
    return redirect('ClubIncharge:student_event_list')

@login_required
def delete_event(request, event_id):
    if not request.session.get('username'):
        print("No username in session")
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        print(f"Attempting to delete event {event_id} by user {username}")
        
        # Get the user details
        user = get_object_or_404(Student, username=username)
        print(f"User role: {user.role}")
        
        # Only Super Admin can delete events
        if user.role != 'Super Admin':
            print(f"Access denied. User role: {user.role}")
            messages.error(request, "Access denied. Only Super Admins can delete events.")
            return redirect('ClubIncharge:ClubIncHome')
        
        # Get the event
        event = get_object_or_404(Event, id=event_id)
        event_title = event.title
        
        if request.method != 'POST':
            messages.error(request, "Invalid request method. Please use the delete button.")
            return redirect('ClubIncharge:ClubIncHome')
        
        try:
            with transaction.atomic():
                # Delete registrations
                registrations = EventRegistration.objects.filter(event=event)
                registrations.delete()
                
                # Delete event
                event.delete()
                messages.success(request, f"Event '{event_title}' has been deleted successfully.")
                
        except Exception as e:
            print(f"Error during deletion: {str(e)}")
            messages.error(request, f"Error deleting event: {str(e)}")
            
        return redirect('SuperAdmin:SuperAdminHome')
        
    except Student.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login')
    except Event.DoesNotExist:
        messages.error(request, "Event not found.")
        return redirect('SuperAdmin:SuperAdminHome')

@login_required
def debug_role(request):
    if not request.session.get('username'):
        return JsonResponse({'error': 'No session'})
    
    try:
        username = request.session.get('username')
        user = Student.objects.get(username=username)
        return JsonResponse({
            'username': username,
            'role': user.role,
            'role_type': str(type(user.role)),
            'is_club_incharge': user.role == 'Club Incharge'
        })
    except Exception as e:
        return JsonResponse({'error': str(e)})
    
# def club_events_list(request):
#     if not request.session.get('username'):
#         messages.error(request, "Please login first")
#         return redirect('login')

#     try:
#         username = request.session.get('username')
#         student = Student.objects.get(username=username)
#         k=len(student.username)
#         # Verify club incharge role
#         if k!= 6:
#             messages.error(request, "Access denied. Only Club Incharge can view this page.")
#             return redirect('Student:student_home')
        
#         # Get all events with participants
#         events = Event.objects.all().order_by('-start_date')
        
#         # Get participants for each event
#         event_participants = {}
#         for event in events:
#             participants = EventRegistration.objects.filter(
#                 event=event
#             ).select_related('student')
#             event_participants[event.id] = participants
        
#         context = {
#             'events': events,
#             'event_participants': event_participants,
#             'student': student
#         }
#         return render(request, 'club_events_list.html', context)
#     except Student.DoesNotExist:
#         messages.error(request, "Student not found.")
#         return redirect('login')


    

def my_events(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        incharge = Student.objects.get(username=username)
        
        # Verify club incharge role
        if incharge.role != 'Club Incharge':
            messages.error(request, "Access denied. Only Club Incharges can view this page")
            return redirect('Student:student_home')
        
        # Get all events created by this club incharge
        events = Event.objects.filter(event_incharge=incharge).order_by('-created_at')
        
        context = {
            'events': events,
            'incharge': incharge
        }
        return render(request, 'my_events.html', context)
    except Student.DoesNotExist:
        messages.error(request, "User not found")
        return redirect('login')
    

def view_participants(request, event_id):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        incharge = Student.objects.get(username=username)
        
        # Get the event
        event = Event.objects.get(id=event_id)
        
        # Get all registrations for this event
        registrations = EventRegistration.objects.filter(event=event).select_related('student')
        
        # Calculate attendance statistics
        total_registrations = registrations.count()
        present_count = registrations.filter(attended=True).count()
        absent_count = total_registrations - present_count
        
        # Calculate attendance percentage
        attendance_percentage = (present_count / total_registrations * 100) if total_registrations > 0 else 0
        
        context = {
            'event': event,
            'registrations': registrations,
            'present_count': present_count,
            'absent_count': absent_count,
            'attendance_percentage': round(attendance_percentage, 1)
        }
        
        return render(request, 'ClubIncharge/view_participants.html', context)
        
    except Event.DoesNotExist:
        messages.error(request, "Event not found")
        return redirect('ClubIncharge:my_events')
    except Student.DoesNotExist:
        messages.error(request, "User not found")
        return redirect('login')
    

@require_POST
def toggle_attendance(request):
    if not request.session.get('username'):
        return JsonResponse({'success': False, 'message': 'Please login first'})
    
    try:
        registration_id = request.POST.get('registration_id')
        registration =EventRegistration.objects.get(id=registration_id)
        
        # Verify the club incharge has permission for this event
        username = request.session.get('username')
        incharge = Student.objects.get(username=username)
        if incharge.role != 'Club Incharge' or registration.event.club != incharge.club:
            return JsonResponse({'success': False, 'message': 'Permission denied'})
        
        # Toggle attendance
        registration.attended = not registration.attended
        registration.save()
        
        return JsonResponse({
            'success': True,
            'attended': registration.attended
        })
        
    except (EventRegistration.DoesNotExist, Student.DoesNotExist):
        return JsonResponse({'success': False, 'message': 'Registration not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    

def take_attendance(request, event_id):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        incharge = Student.objects.get(username=username)
        
        if incharge.role != 'Club Incharge':
            messages.error(request, "Access denied. Only Club Incharges can take attendance")
            # return redirect('Student:student_home')
        
        event = get_object_or_404(Event, id=event_id)
        registrations = EventRegistration.objects.filter(event=event)

        # Handle attendance submission
        if request.method == 'POST':
            for registration in registrations:
                attendance_key = f'attendance_{registration.id}'
                is_present = request.POST.get(attendance_key) == 'present'
                registration.attended = is_present
                registration.save()
            messages.success(request, "Attendance updated successfully!")
            return redirect('ClubIncharge:take_attendance', event_id=event_id)

        context = {
            'event': event,
            'registrations': registrations,
            'incharge': incharge
        }
        return render(request, 'take_attendance.html', context)
        
    except Student.DoesNotExist:
        messages.error(request, "User not found")
        return redirect('login')
    


    
