from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Student, Teacher, User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
