# students/models.py

from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) # Increased length for hashed password
    date_of_birth = models.DateField()
    major = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return self.name

class Course(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
