from django.urls import path
from . import views
app_name = "student_portal"
urlpatterns = [
    path('student_detail/',views.studentDetail,name="student_detail"),
    path('logout/',views.logout,name="logout"),
    path('class_detail/<int:id>/',views.classDetail,name='class_detail'),
    path('class_detail/<int:id>/students',views.students,name="students"),
]