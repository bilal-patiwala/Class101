
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth
from TeacherPortal.models import CreateClass
from account.models import Student


# Create your views here.
def studentDetail(request):
    student = Student.objects.get(user=request.user)
    classes = reversed(CreateClass.objects.filter(student=student))

    if request.method == 'POST':
        student.student_profile_pic = request.FILES['edit_profile']
        student.save()
        return redirect('student_portal:student_detail')

    context = {
        'classes':classes,
        'student':student,
    }
    return render(request,'StudentPortal/student_detail_page.html',context)

def logout(request):
    auth.logout(request)
    return redirect('account:welcome') 

def classDetail(request,id):
    student = Student.objects.get(user=request.user)
    context = {
        'class_detail': get_object_or_404(CreateClass, pk=id),
        'student':student,
        'id':id,
    }
    return render(request,'StudentPortal/class_detail.html',context)

def students(request,id):
    student = Student.objects.get(user=request.user)
    classroom = get_object_or_404(CreateClass,pk=id)
    students = classroom.student.all().order_by("name")
    context = {
        'class_detail': get_object_or_404(CreateClass, pk=id),
        'student':student,
        'id':id,
        'students' : students,
    }
    return render(request,'StudentPortal/students.html',context)
