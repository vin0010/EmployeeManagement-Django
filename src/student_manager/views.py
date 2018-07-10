from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Student

from .forms import StudentForm
# Create your views here.

def get_student(request, id=0):
    student_instance = Student.objects.get(id=id)
    context = {
        "student": student_instance
    }
    return render(request, "view_student.html", context)
    # return HttpResponse("<h1>Welcome Student<h1>")

def get_student1(request, id=0):
    student_instance = Student.objects.get(id=id)
    context = {
        "student": student_instance
    }
    return render(request, "view_student.html", context)
    # return HttpResponse("<h1>Welcome Student<h1>")

def create_student(request):
    if request.method == "POST":
        print(request.POST)
    form = StudentForm()
    context = {
        "form":form
    }
    # return HttpResponse("<h1>Welcome Student Form<h1>")
    return render(request, "create_student.html", context)

def get_all_student(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    # return HttpResponse("<h1>All student<h1>")
    return render(request, "view_all_students.html", context)
