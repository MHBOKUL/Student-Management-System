from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'student/index.html',{
        'student': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(request, reverse ("home"))

    
def add (request):
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_Student_number = form.cleaned_data["Student_number"]
            new_F_name = form.cleaned_data["F_name"]
            new_L_name = form.cleaned_data["L_name"]
            new_email= form.cleaned_data["email"]
            new_gpa = form.cleaned_data["gpa"]
            
            New_student = Student (
                Student_number = new_Student_number, 
                F_name=new_F_name ,
                L_name= new_L_name ,
                email= new_email,
                gpa = new_gpa ,

            )
            New_student.save()
            return render(request, 'student/add.html',
            {
                'form': StudentForm(),
                'success': True
            })
            
    else:
        form = StudentForm()
        return render (request, 'student/add.html',{
            'form': StudentForm()
        })
def edit(request, id):
    # Retrieve the student instance
    student = get_object_or_404(Student, pk=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'student/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)

    return render(request, 'student/edit.html', {
        'form': form,
        'student': student
    })
    
def delete(request,id):
    if request.method =="POST":
        student= Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('home'))
    