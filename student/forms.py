from django import forms
from .models import*

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ["Student_number", "F_name", "L_name","email", "gpa"]
        labels = {
            "Student_number" : "Student_number",
            "F_name": "F_name",
            "L_name" : "L_name",
            "email": "email", 
            "gpa": "GPA",
        }
Widget ={
     "Student_number" : forms.NumberInput(attrs={"class": "form-control"}),
            "F_name": forms.TextInput(attrs={"class": "form-control"}),
            "L_name" : forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}), 
            "gpa": forms.NumberInput(attrs={"class": "form-control"}),
}