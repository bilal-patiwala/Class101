from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('',views.Welcome.as_view(), name="welcome"),
    path('teacher-registration/',views.TeacherRegistration.as_view(),name='teacher-register'),
    path('student-registration/',views.StudentRegistration.as_view(),name='student-register'),
]