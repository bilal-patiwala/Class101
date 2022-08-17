from multiprocessing import context
from turtle import st
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from TeacherPortal.models import CreateClass
from account.models import Student, Teacher
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def teacherDetail(request):
    teacher = Teacher.objects.get(user=request.user)
    teacher_name = request.user.username
    if request.method == 'POST':
        if request.POST.get('create_class'):
            class_name = request.POST['class_name']
            section = request.POST['section']
            subject_name = request.POST['subject_name']

            if class_name == "":
                messages.warning(request,'class name is empty ')
                return redirect('teacher_portal:teacher_detail')

            new_class = CreateClass.objects.create(teacher=teacher,class_name=class_name,section=section,subject_name=subject_name)
            new_class.save()
            return redirect('teacher_portal:teacher_detail')

        if request.POST.get('edit_image'):
            teacher.teacher_profile_pic = request.FILES['edit_profile']
            teacher.save()
            return redirect('teacher_portal:teacher_detail')
    
    

    classes = reversed(CreateClass.objects.filter(teacher=teacher))
    context = {
        'teacher':teacher,
        'teacher_name':teacher_name,
        'classes':classes
    }

    return render(request,'TeacherPortal/teacher_detail_page.html',context)

def logout(request):
    auth.logout(request)
    return redirect('account:welcome')  


def classDetail(request,id):
    teacher = Teacher.objects.get(user=request.user)
    context = {
        'class_detail': get_object_or_404(CreateClass, pk=id),
        'teacher':teacher,
        'id':id,
    }
    
    return render(request,'TeacherPortal/class_detail.html',context)

def students(request,id):
    teacher = Teacher.objects.get(user=request.user)
    if request.method == 'POST':
        email = request.POST['email']
        roll_no = request.POST['roll_no']
        if Student.objects.filter(email=email,roll_no=roll_no).exists():
            student = Student.objects.get(email=email,roll_no=roll_no)
            current_class = get_object_or_404(CreateClass,pk=id)
            current_class.student = student
            current_class.save()
            return redirect('teacher_portal:students',id=id)
        else:
            messages.error(request, 'student does not exist')


    context = {
        'class_detail': get_object_or_404(CreateClass, pk=id),
        'teacher':teacher,
        'id':id,
    }
    return render(request,'TeacherPortal/students.html',context)