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

