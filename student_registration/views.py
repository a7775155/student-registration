# student_registration/views.py

from django.shortcuts import render

def home(request):
    """
    A simple view for the project's home page.
    """
    return render(request, 'home.html')
