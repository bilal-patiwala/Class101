from django.urls import path
from . import views

app_name = "teacher_portal"
urlpatterns = [
    path('teacher_detail/',views.teacherDetail,name="teacher_detail"),
    path('logout/',views.logout,name='logout'),
    path('class_detail/<int:id>',views.classDetail ,name='class_detail'),
]