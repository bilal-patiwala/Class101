from django.shortcuts import render

# Create your views here.
def studentDetail(request):
    return render(request,'StudentPortal/student_detail_page.html')