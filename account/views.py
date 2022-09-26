

# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib import messages
from django.urls import reverse

from django.views import View

from account.models import Student, Teacher
User = get_user_model()

# Create your views here.

class Welcome(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_teacher == True:
                return redirect(reverse('teacher_portal:teacher_detail'))
            if request.user.is_student == True:
                return redirect(reverse('student_portal:student_detail'))

        return render(request, 'account/base.html',)
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username,email=email,password=password)

        if user is not None:
            if user.is_teacher == True:
                auth.login(request,user)
                return redirect(reverse('teacher_portal:teacher_detail'))
            if user.is_student == True:
                auth.login(request,user)
                return redirect(reverse('student_portal:student_detail'))
                
        else:
            messages.error(request,'invalid username or password')
            return redirect('account:welcome')


class TeacherRegistration(View):

    def __init__(self):
        self.user_type = 'teacher'
        self.registered = False

    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_teacher == True:
                return redirect(reverse('teacher_portal:teacher_detail'))
        
        return render(request,'account/teacher-registration.html')


    def post(self,request):
        name = request.POST['name']
        username = request.POST['username']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username not available')
                return redirect('account:teacher-register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                user.is_teacher=True
                user.save()

                teacher = Teacher.objects.create(user=user,name=name,email=email,phone=phone_no)
                teacher.save()
                self.registered = True
                auth.login(request,user)
                return redirect(reverse('teacher_portal:teacher_detail'))
        else:
            messages.error(request,' password not matched ')
            return redirect('account:teacher-register')


class StudentRegistration(View):

    def __init__(self):
        self.user_type = 'student'
        self.registered = False
    
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.is_student == True:
                return redirect(reverse('student_portal:student_detail'))

        return render(request,'account/student-registration.html')
    
    def post(self,request):
        name = request.POST['name']
        username = request.POST['username']
        roll_no = request.POST['roll_no']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username not available')
                return redirect('account:student-register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                user.is_student = True
                user.save()

                student = Student.objects.create(user=user,name=name,roll_no=roll_no,email=email,phone=phone_no)
                student.save()

                registered = True
                auth.login(request,user)
                return redirect(reverse('student_portal:student_detail'))
        else:
            messages.error(request,' password not matched ')
            return redirect('account:student-register')