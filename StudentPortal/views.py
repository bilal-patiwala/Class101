from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from TeacherPortal.models import CreateClass
from account.models import Student


# Create your views here.
def studentDetail(request):
    student = Student.objects.get(user=request.user)
    classes = reversed(CreateClass.objects.filter(student=student))
    context = {
        'classes':classes,
    }
    return render(request,'StudentPortal/student_detail_page.html',context)

def logout(request):
    auth.logout(request)
    return redirect('account:welcome') 