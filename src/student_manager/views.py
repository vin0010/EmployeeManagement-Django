from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Student


# Create your views here.

def get_student(request, id=0):
    student_instance = Student.objects.get(id=id)
    context = {
        "student": student_instance
    }
    return render(request, "view_student.html", context)
    # return HttpResponse("<h1>Welcome Student<h1>")


def get_all_student(request):
    return HttpResponse("<h1>All student<h1>")
