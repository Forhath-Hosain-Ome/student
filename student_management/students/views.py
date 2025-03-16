from django.shortcuts import render, get_object_or_404, redirect
from .models import student
from .forms import StudentForm
from django.contrib import messages

def index(request):
    return render(request, 'base.html')

def student_list(request):
    students = student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, 'Student deleted successfully')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})