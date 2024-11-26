from django.db import models

# Create your models here.
 
class Student(models.Model):
    name =  models.CharField(max_length=100)
    registration_no = models.CharField (max_length = 20, unique=True)
    email =  models.EmailField (unique=True, null=True)
    room_no  = models.IntegerField()
    section_choice = [
        ("A","A"),
        ("B","B"),
        ("C","C"),
    ]
    section = models.CharField(max_length = 1, choices=section_choice)
    created_at =  models.DateTimeField (auto_now_add=True)
    updated_at =  models.DateTimeField (auto_now_add=False , auto_now = False , null=True ,blank=True) 

class EducationHistory(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE, related_name="eduction_history")
    institution_name  = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study  = models.CharField(max_length=100)
    start_date =  models.DateField()
    end_date   = models.DateField(null=True)
    grade  = models.CharField(max_length=10, null=True)

class Certificate(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE, related_name="certificates")
    certificate_name = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    date_issued = models.DateField()
    description = models.TextField(null=True, blank=True)
    certificate_file = models.FileField(upload_to='certificates/' , null=True , blank= True)
 


