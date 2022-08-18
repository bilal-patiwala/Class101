from django.urls import path
from . import views

app_name = "teacher_portal"
urlpatterns = [
    path('teacher_detail/',views.teacherDetail,name="teacher_detail"),
    path('logout/',views.logout,name='logout'),
    path('class_detail/<int:id>/',views.classDetail ,name='class_detail'),
    path('class_detail/<int:id>/students/',views.students,name='students'),
    path('class_detail/<int:id>/classwork/',views.classwork,name='classwork'),
]