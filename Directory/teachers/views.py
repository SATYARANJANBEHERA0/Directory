from django.shortcuts import render

# Create your views here.
# teachers/views.py
from django.shortcuts import render
from .models import Teacher

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})

def teacher_import(request):
    # Implement the teacher import view here
    return render(request, 'teachers/teacher_import.html')
