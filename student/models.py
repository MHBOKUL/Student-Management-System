from django.db import models

# Create your models here.
class Student(models.Model):
    Student_number = models.PositiveIntegerField()
    F_name = models.CharField(max_length=200)
    L_name = models.CharField(max_length=200)
    email =models.EmailField(max_length=70)
    gpa = models.FloatField()
    
    def __str__(self):
        return f'Student : {self.F_name} {self.L_name}'