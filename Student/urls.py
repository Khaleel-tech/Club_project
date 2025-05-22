from django.urls import path
from . import views

app_name = 'Student'

urlpatterns = [
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('home/', views.student_home, name='student_home'),
    # path('profile/', views.student_profile, name='student_profile'),
    path('events/', views.student_event_list, name='student_events'),
    path('event/register/<int:event_id>/', views.register_event, name='register_event'),
    path('event/unregister/<int:event_id>/', views.unregister_event, name='unregister_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('my-registered-events/', views.my_registered_events, name='my_registered_events'),
    path('view-profile/', views.view_profile, name='view_profile'),
]
