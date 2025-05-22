from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
   path("SuperAdminHome/",views.SuperAdminHome,name="SuperAdminHome"),
   path("AddStudent/",views.add_student,name="AddStudent"),
   path("ViewStudent/",views.view_students,name="ViewStudent"),
   path('success/<str:username>/', views.success, name='success'),
   path('student/<str:username>/', views.student_profile, name='student_profile'),
   path('create-event/', views.create_event, name='create_event'),
   path('my-events/', views.my_events, name='my_events'),
   path('view-participants/<int:event_id>/', views.view_participants, name='view_participants'),
   path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
   path('take-attendance/<int:event_id>/', views.take_attendance, name='take_attendance'),
]
