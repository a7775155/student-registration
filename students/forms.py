# students/forms.py

from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    """
    A form to handle student registration.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'password', 'date_of_birth', 'major']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class StudentLoginForm(forms.Form):
    """
    A form to handle student login.
    """
    student_id = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

class StudentProfileForm(forms.ModelForm):
    """
    A form for editing a student's profile.
    This form excludes the student_id and password fields.
    """
    class Meta:
        model = Student
        fields = ['name', 'email', 'date_of_birth', 'major']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
