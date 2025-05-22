from django.shortcuts import render
from ClubIncharge import urls,views
from Student import urls,views
from ClubIncharge.views import ClubIncHome
from Student.models import EventRegistration
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from ClubIncharge.models import Event
from ClubIncharge.forms import EventForm
from django.utils import timezone
from SuperAdmin.models import Student  # Changed this import
from django.contrib.auth.models import Group
from Student.models import EventRegistration  # Add this import
from django.core.cache import cache
from django.db.models import Q
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.

def home(request):
    return render(request, 'home.html')

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

def login(request):
    return render(request,'login.html')


# @login_required()
def SuperAdminHome(request):
  
        if not request.session.get('username'):
            messages.error(request, "Please login first")
            return redirect('login')
    
        # Add print statement for debugging
        print("Session in SuperAdminHome:", request.session.get('name'))
    
        context = {
            'name': request.session.get('name')  # Add name to context
        }
        return render(request, 'SuperAdminHome.html', context)


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CompleteProfileForm, InitialStudentForm, LoginForm
from .models import Student
from django.db.models import F
from django.db.models.functions import Length

from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Student  # Ensure this import matches your project structure
from .forms import LoginForm  # Ensure this import matches your project structure

def login_view(request):
    print("Login attempt:", request.method)
    
    # Redirect authenticated users to their respective home pages
    if request.user.is_authenticated:
        role = request.session.get('role')
        if role == 'SuperAdmin':
            return redirect('SuperAdminHome')
        elif role == 'ClubIncharge':
            return redirect('ClubIncharge:ClubIncHome')
        elif role == 'ReportManager':
            return redirect('ReportManager')
        elif role == 'Student':
            return redirect('Student:student_home')

    if request.method == "POST":
        print("POST data:", request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = Student.objects.get(username=username)
                if len(username) == 4 and user.password == password:
                    print("SuperAdmin login successful")
                    print("Name:", user.name)
                    request.session['username'] = username
                    request.session['name'] = user.name
                    request.session['role'] = user.role
                    return redirect('SuperAdminHome')
                elif len(username) == 6 and user.password == password:
                    request.session['username'] = username
                    request.session['name'] = user.name
                    request.session['role'] = user.role
                    if not user.is_profile_complete:
                        messages.info(request, "Please complete your profile first")
                        return redirect('ClubIncharge:complete_profile')
                    else:
                        return redirect('ClubIncharge:ClubIncHome')
                elif len(username) == 8 and user.password == password:
                    request.session['username'] = username
                    request.session['name'] = user.name
                    request.session['role'] = user.role
                    if not user.is_profile_complete:
                        messages.info(request, "Please complete your profile first")
                        return redirect('ReportManager:complete_profile')
                    else:
                        return redirect('ReportManager')
                elif len(username) == 10 and user.password == password:
                    request.session['username'] = username
                    request.session['name'] = user.name
                    request.session['role'] = user.role
                    if not user.is_profile_complete:
                        messages.info(request, "Please complete your profile first")
                        return redirect('Student:complete_profile')
                    else:
                        return redirect('Student:student_home')
                else:
                    messages.error(request, "Invalid password.")
            except Student.DoesNotExist:
                messages.error(request, "Invalid username or role.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
# def complete_profile(request):
#     if not request.session.get('username'):
#         messages.error(request, "Please login first")
#         return redirect('login')
        
#     try:
#         student = Student.objects.get(username=request.session['username'])
#         if student.is_profile_complete:
#             if student.role == 'Student':
#                 return redirect('Student:student_home')
#             elif student.role == 'Club Incharge':
#                 return redirect('ClubIncharge:ClubIncHome')
#             elif student.role == 'Report Manager':
#                 return redirect('ReportManager')
#             elif student.role == 'Super Admin':
#                 return redirect('SuperAdminHome')
            
#         # Generate email if it doesn't exist
#         if not student.email:
#             student.email = f"{student.username}@kluniversity.in"
#             student.save()
            
#         if request.method == 'POST':
#             form = CompleteProfileForm(request.POST, instance=student)
#             if form.is_valid():
#                 student = form.save(commit=False)
#                 student.is_profile_complete = True
#                 student.save()
#                 messages.success(request, "Profile completed successfully!")
#                 if student.role == 'Student':
#                     return redirect('Student:student_home')
#                 elif student.role == 'Club Incharge':
#                     return redirect('ClubIncharge:ClubIncHome')
#                 elif student.role == 'Report Manager':
#                     return redirect('ReportManager')
#                 elif student.role == 'Super Admin':
#                     return redirect('SuperAdminHome')
#         else:
#             form = CompleteProfileForm(instance=student)
            
#         # Add student to context
#         context = {
#             'form': form,
#             'student': student,  # Make sure student is in context
#             'residence': student.residence,
#             'gender': student.gender,
#             'transport': student.transport,
#             'hostel_boys_campus': student.hostel_boys_campus,
#             'country': student.country
#         }
        
#         # Handle auto-updates
#         if request.POST.get('auto_update') == 'true':
#             form = CompleteProfileForm(request.POST, instance=student)
#             if form.is_valid():
#                 student = form.save()
#                 if student.role == 'Student':
#                     return redirect('Student:student_home')
#                 elif student.role == 'Club Incharge':
#                     return redirect('ClubIncharge:ClubIncHome')
#                 elif student.role == 'Report Manager':
#                     return redirect('ReportManager')
#                 elif student.role == 'Super Admin':
#                     return redirect('SuperAdminHome')
            
#         return render(request, 'Student/complete_profile.html', context)
        
#     except Student.DoesNotExist:
#         messages.error(request, "Student not found")
#         return redirect('login')



def AddStudent(request):
    return render(request,'AddStudent.html')

def ViewStudent(request):
    return render(request,'ViewStudent.html')

# views.py
from django.shortcuts import render, redirect
from .forms import StudentForm

def add_student(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
        
    if request.method == 'POST':
        form = InitialStudentForm(request.POST)
        # Get username from form data, not form object
        username = request.POST.get('username')
        
        if username and Student.objects.filter(username=username).exists():
            messages.error(request, f"Student with username {username} already exists!")
            return render(request, 'AddStudent.html', {'form': form})
            
        if form.is_valid():
            student = form.save(commit=False)
            student.password = student.username
            student.is_profile_complete = False
            student.save()
            # messages.success(request, f"Student {student.username} added successfully!")
            return redirect('success', username=student.username)
    else:
        form = InitialStudentForm()
    return render(request, 'AddStudent.html', {'form': form})

def add_student(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
        
    if request.method == 'POST':
        form = InitialStudentForm(request.POST)
        # Get username from form data, not form object
        username = request.POST.get('username')
        
        
        
        if username and Student.objects.filter(username=username).exists():
            messages.error(request, f"Student with username {username} already exists!")
            return render(request, 'AddStudent.html', {'form': form})
            
        if form.is_valid():
            student = form.save(commit=False)
            student.password = student.username
            student.is_profile_complete = False
            student.save()
            
            # messages.success(request, f"Student {student.username} added successfully!")
            return redirect('success', username=student.username)
    else:
        form = InitialStudentForm()
    return render(request, 'AddStudent.html', {'form': form})

def success(request, username):
    return render(request, 'Success.html', {'username': username})

def view_students(request):
    search_query = request.GET.get('search', '')
    role_filter = request.GET.get('role', 'All')

    if role_filter == 'All':
        students = Student.objects.all()
    else:
        students = Student.objects.filter(role=role_filter)

    if search_query:
        students = students.filter(username__icontains=search_query)

    context = {
        'students': students,
        'search_query': search_query,
        'role_filter': role_filter,
    }
    return render(request, 'ViewStudent.html', context)

def student_profile(request, username):
    try:
        student = Student.objects.get(username=username)
        registrations = EventRegistration.objects.filter(student=student).select_related('event')
        total_events = registrations.count()
        attended_events = registrations.filter(attended=True).count()
        
        # Calculate attendance rate
        attendance_rate = int((attended_events / total_events * 100) if total_events > 0 else 0)
        
        context = {
            'student': student,
            'registrations': registrations,
            'total_events': total_events,
            'attended_events': attended_events,
            'attendance_rate': attendance_rate  # Add calculated rate to context
        }
        return render(request, 'student_profile.html', context)
    except Student.DoesNotExist:
        messages.error(request, "Student not found")
        return redirect('view_students')

      
      
# @login_required
def create_event(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
        
    try:
        username = request.session.get('username')
        user = Student.objects.get(username=username)
        
        # Allow both Super Admin and Club Incharge to create events
        if user.role not in ['Super Admin']:
            messages.error(request, "Access denied. Only Super Admins can create events")
            return redirect('Student:student_home')
        
        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                event = form.save()
                messages.success(request, 'Event created successfully!')
                # Redirect based on role
                if user.role == 'Super Admin':
                    return redirect('SuperAdminHome')
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


# @login_required
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
        messages.error(request, "User not found.")
        return redirect('SuperAdmin:SuperAdminHome')




# @login_required
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
        
        if request.method == 'POST':
            messages.error(request, "Invalid request method. Please use the delete button.")
            return redirect('SuperAdminHome')
        
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
            
        return redirect('my_events')
        
    except Student.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login')
    except Event.DoesNotExist:
        messages.error(request, "Event not found.")
        return redirect('SuperAdmin:SuperAdminHome')

# @login_required
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
    
def my_events(request):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        incharge = Student.objects.get(username=username)
        
        # Verify Super admin role
        if incharge.role != 'Super Admin':
            messages.error(request, "Access denied. Only Super Admins can view this page")
            # return redirect('Student:student_home')
        
        # Get all events created by this club incharge
        events = Event.objects.order_by('-created_at')
        
        context = {
            'events': events,
            # 'incharge': incharge
        }
        return render(request, 'SuperAdmin/my_events.html',context)
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
        
        return render(request, 'view_participants.html', context)
        
    except Event.DoesNotExist:
        messages.error(request, "Event not found")
        return redirect('my_events')
    except Student.DoesNotExist:
        messages.error(request, "User not found")
        return redirect('login')
    
    
def take_attendance(request, event_id):
    if not request.session.get('username'):
        messages.error(request, "Please login first")
        return redirect('login')
    
    try:
        username = request.session.get('username')
        incharge = Student.objects.get(username=username)
        
        if incharge.role != 'Super Admin':
            messages.error(request, "Access denied. Only Super Admin can take attendance")
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
            return redirect('take_attendance', event_id=event_id)

        context = {
            'event': event,
            'registrations': registrations,
            'incharge': incharge
        }
        return render(request, 'take_attendance.html', context)
        
    except Student.DoesNotExist:
        messages.error(request, "User not found")
        return redirect('login')
    

def some_protected_view(request):
    student = request.user.student
    if not student.is_step2_complete():
        return redirect('complete_basic_info')
    if not student.is_step3_complete():
        return redirect('complete_academic_info')
    # ... and so on
    

# def complete_profile(request):
#     if request.method == 'POST':
#         form = CompleteProfileForm(request.POST, instance=student)
#         if form.is_valid():
#             student = form.save(commit=False)
#             # The password will be automatically set in the save method
#             student.save()
#             messages.success(request, "Profile completed successfully! Your password has been set to your date of birth (YYYYMMDD)")
#             return redirect('student_home')

