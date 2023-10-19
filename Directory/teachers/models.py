from django.db import models

# Create your models here.



class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='teacher_profile_pics/')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    room_number = models.CharField(max_length=10)
    employee_number = models.CharField(max_length=10)
    subjects_taught = models.CharField(max_length=200)
