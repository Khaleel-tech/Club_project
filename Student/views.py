from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ClubIncharge.models import Event
from SuperAdmin.forms import CompleteProfileForm
from SuperAdmin.models import Student
from .models import EventRegistration
from django.utils import timezone
from datetime import timedelta




# from django.shortcuts import render, redirect
# from django.contrib import messages
# # from .models import Student
# # from .forms import CompleteProfileForm

# def complete_profile(request):
#     if not request.session.get('username'):
#         messages.error(request, "Please login first")
#         return redirect('login')

#     try:
#         student = Student.objects.get(username=request.session['username'])

#         # Check if the request is for viewing or updating the profile
#         if request.method == 'GET' and student.is_profile_complete:
#             # If profile is already complete and it's a GET request, just show the profile
#             form = CompleteProfileForm(instance=student)
#             context = {
#                 'form': form,
#                 'gender': student.gender,
#                 'residence': student.residence,
#                 'transport': student.transport,
#                 'hostel_boys_campus': student.hostel_boys_campus,
#                 'country': student.country,
#             }
#             return render(request, 'Student/complete_profile.html', context)

#         if request.method == 'POST':
#             form = CompleteProfileForm(request.POST, instance=student)
#             is_auto_update = request.POST.get('auto_update') == 'true'

#             if form.is_valid() and not is_auto_update:
#                 student = form.save(commit=False)
#                 # student.email = f"{student.username}@kluniversity.in"

#                 if not student.is_profile_complete:
#                     # Redirect only if the profile was just completed
#                     student.is_profile_complete = True
#                     student.save()
#                     messages.success(request, "Profile completed successfully!")

#                     if student.role == 'Student':
#                         return redirect('Student:student_home')
#                     elif student.role == 'Club Incharge':
#                         return redirect('ClubIncharge:ClubIncHome')
#                     elif student.role == 'Report Manager':
#                         return redirect('ReportManager')
#                     elif student.role == 'Super Admin':
#                         return redirect('SuperAdminHome')
#                 else:
#                     # If profile was already complete, just save and show the profile
#                     student.save()
#                     messages.success(request,"Profile updated successfully!")

#         # If not a POST request or profile was not just completed, render the form
#         form = CompleteProfileForm(instance=student)
#         context = {
#             'form': form,
#             'gender': request.POST.get('gender', student.gender),
#             'residence': request.POST.get('residence', student.residence),
#             'transport': request.POST.get('transport', student.transport),
#             'hostel_boys_campus': request.POST.get('hostel_boys_campus', student.hostel_boys_campus),
#             'country': request.POST.get('country', student.country),
#         }
#         return render(request, 'Student/complete_profile.html', context)

#     except Student.DoesNotExist:
#         messages.error(request, "Student not found")
#         return redirect('login')




def complete_profile(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
        
    try:
        student = Student.objects.get(username=request.session['username'])
        
        if student.is_profile_complete:
            if student.role == 'Student':
                return redirect('Student:student_home')
            elif student.role == 'Club Incharge':
                return redirect('ClubIncharge:ClubIncHome')
            elif student.role == 'Report Manager':
                return redirect('ReportManager')
            elif student.role == 'Super Admin':
                return redirect('SuperAdminHome')
            
        if request.method == 'POST':
            form = CompleteProfileForm(request.POST, instance=student)
            
            # student.is_profile_complete = False
            # Check if this is an auto-update request
            is_auto_update = request.POST.get('auto_update') == 'true'
            
            if form.is_valid() and not is_auto_update:
                student = form.save(commit=False)
                # student.email = f"{student.username}@kluniversity.in"
                student.is_profile_complete = True
                student.save()
                messages.success(request, "Profile completed successfully!")
                if student.role == 'Student':
                    return redirect('Student:student_home')
                elif student.role == 'Club Incharge':
                    return redirect('ClubIncharge:ClubIncHome')
                elif student.role == 'Report Manager':
                    return redirect('ReportManager')
                elif student.role == 'Super Admin':
                    return redirect('SuperAdminHome')
        else:
            form = CompleteProfileForm(instance=student)

        # Always include these context variables
        context = {
            'form': form,
            'gender': request.POST.get('gender', student.gender),
            'residence': request.POST.get('residence', student.residence),
            'transport': request.POST.get('transport', student.transport),
            'hostel_boys_campus': request.POST.get('hostel_boys_campus', student.hostel_boys_campus),
            'country': request.POST.get('country', student.country),
            'password': request.POST.get('password', student.password),
        }
        return render(request, 'Student/complete_profile.html', context)
            
    except Student.DoesNotExist:
        messages.error(request, "Student not found")
        return redirect('login')

# def complete_profile(request):
#     if not request.session.get('username'):
#         messages.error(request, "Please login first")
#         return redirect('login')
        
#     try:
#         student = Student.objects.get(username=request.session['username'])
#         if student.is_profile_complete:
#             return redirect('Student:student_home')
            
#         if request.method == 'POST':
#             form = CompleteProfileForm(request.POST, instance=student)
#             if form.is_valid():
#                 form.save()
#                 student.is_profile_complete = True
#                 student.save()
#                 messages.success(request, "Profile completed successfully!")
#                 return redirect('Student:student_home')
#             else:
#                 for field, errors in form.errors.items():
#                     for error in errors:
#                         messages.error(request, f"{field}: {error}")
#         else:
#             form = CompleteProfileForm(instance=student)
            
#         return render(request, 'Student/complete_profile.html', {'form': form})
        
#     except Student.DoesNotExist:
#         messages.error(request, "Student not found")
#         return redirect('login')



# @login_required
def student_home(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')

    try:
        username = request.session.get('username')
        student = Student.objects.get(username=username)
        
        # Add strict role verification
        if student.role == 'Club Incharge':
            messages.error(request, "Access denied. Please use the Club Incharge portal.")
            return redirect('ClubIncharge:ClubIncHome')
        
        context = {
            'student': student,
            'branch_names': dict(Student.Branch_choices),
            'year_names': dict(Student.Year_choices),
            'training_names': dict(Student.Training_Choices)
        }
        return render(request, 'Student/StudentHomePage.html', context)
    except Student.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('login')

# 
# @login_required
def student_event_list(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')

    try:
        username = request.session.get('username')
        student = Student.objects.get(username=username)
        
        # Get current date
        current_date = timezone.now().date()
        date_before = current_date - timedelta(days=2)
        date_after = current_date + timedelta(days=2)
        
        # Get events within ±2 days using start_date
        events = Event.objects.filter(
            start_date__gte=date_before,
            start_date__lte=date_after
        ).order_by('-created_at')
        
        registered_events = EventRegistration.objects.filter(
            student=student
        ).values_list('event_id', flat=True)

        context = {
            'events': events,
            'registered_events': registered_events,
            'student': student
        }
        return render(request, 'Student/student_events.html', context)
    except Student.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('login')

# @login_required
def register_event(request, event_id):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        student = Student.objects.get(username=username)
        event = Event.objects.get(id=event_id)
        
        # Check if registration is still open
        if not event.is_registration_open():
            messages.error(request, "Registration for this event has closed.")
            return redirect('Student:student_events')
        
        # Check if event is full
        if event.max_participants > 0 and event.participant_count() >= event.max_participants:
            messages.error(request, "Sorry, this event is full!")
            return redirect('Student:student_events')
        
        # Check if student is already registered
        if EventRegistration.objects.filter(event=event, student=student).exists():
            messages.warning(request, "You are already registered for this event!")
        else:
            # Create new registration
            EventRegistration.objects.create(
                event=event,
                student=student
            )
            messages.success(request, f"Successfully registered for {event.title}")
        
        return redirect('Student:student_events')
        
    except Event.DoesNotExist:
        messages.error(request, "Event not found.")
        return redirect('Student:student_events')
    except Student.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('login')

# @login_required
def unregister_event(request, event_id):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        student = Student.objects.get(username=username)
        event = Event.objects.get(id=event_id)
        
        # Try to find and delete the registration
        registration = EventRegistration.objects.filter(
            event=event,
            student=student
        ).first()
        
        if registration:
            registration.delete()
            messages.success(request, f"Successfully unregistered from {event.title}")
        else:
            messages.warning(request, "You were not registered for this event.")
        
        return redirect('Student:student_events')
        
    except Event.DoesNotExist:
        messages.error(request, "Event not found.")
        return redirect('Student:student_events')
    except Student.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('login')

# @login_required
def event_detail(request, event_id):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        student = Student.objects.get(username=username)
        event = Event.objects.get(id=event_id)
        
        # Check if student is registered
        is_registered = EventRegistration.objects.filter(
            event=event,
            student=student
        ).exists()
        
        context = {
            'event': event,
            'student': student,
            'is_registered': is_registered,
            'available_spots': event.get_available_spots(),
            'is_registration_open': event.is_registration_open(),
            'total_registered': event.participant_count()
        }
        
        return render(request, 'Student/event_detail.html', context)
        
    except Event.DoesNotExist:
        messages.error(request, "Event not found.")
        return redirect('Student:student_events')
    except Student.DoesNotExist:
        messages.error(request, "Student not found.")
        return redirect('login')

def my_registered_events(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        student = Student.objects.get(username=username)
        
        # Get all registrations for the student with related event info
        registrations = EventRegistration.objects.filter(student=student).select_related('event')
        
        context = {
            'student': student,
            'registrations': registrations
        }
        return render(request, 'Student/my_registered_events.html', context)
        
    except Student.DoesNotExist:
        messages.error(request, "Student not found")
        return redirect('login')


# @login_required
def view_profile(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        student = Student.objects.get(username=username)
        return render(request, 'Student/view_profile.html', {'student': student})
    except Student.DoesNotExist:
        messages.error(request, "Student not found")
        return redirect('login')
