from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('',views.welcome, name="welcome"),
    path('teacher-registration/',views.teacherRegistration,name='teacher-register'),
    path('student-registration/',views.studentRegistration,name='student-register'),
]