from django.contrib import admin
from django.urls import path
from. import views
from Student import views as Student_views


app_name = 'ClubIncharge'
urlpatterns = [
    path('', views.ClubIncHome, name='ClubIncHome'),  # Root path for club incharge
    path('create-event/', views.create_event, name='create_event'),
    path('event/<int:event_id>/participants/', views.event_participants, name='event_participants'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('debug-role/', views.debug_role, name='debug_role'),
    # path('club/events/', views.club_events_list, name='club_events_list'),
    path('my-events/', views.my_events, name='my_events'),
    path('view-participants/<int:event_id>/', views.view_participants, name='view_participants'),
    path('toggle-attendance/', views.toggle_attendance, name='toggle_attendance'),
    path('take-attendance/<int:event_id>/', views.take_attendance, name='take_attendance'),
    path('complete-profile/', Student_views.complete_profile, name='complete_profile'),
    
]
