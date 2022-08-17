from statistics import mode
from django.db import models
from account.models import Teacher,Student

# Create your models here.

class CreateClass(models.Model):
    teacher = models.ForeignKey(Teacher,related_name="class_teacher",on_delete=models.CASCADE,null=True)
    student = models.ForeignKey(Student,related_name="students",on_delete=models.CASCADE,null=True)
    class_name = models.CharField(max_length=255,null=False)
    section = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)

    def __str__(self):
        return (self.section+" | "+self.subject_name)

