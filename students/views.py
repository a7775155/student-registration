# students/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import StudentRegistrationForm, StudentLoginForm, StudentProfileForm
from django.contrib.auth.hashers import make_password, check_password
from .models import Student, Course

def register_student(request):
    """
    A view that handles both the display and submission of the registration form.
    """
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Correctly hash the password before saving.
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])
            student.save()
            return redirect(reverse('home'))
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'students/register.html', {'form': form})

def login_student(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            password = form.cleaned_data['password']
            
            try:
                student = Student.objects.get(student_id=student_id)
                if check_password(password, student.password):
                    # Store the student_id in the session
                    request.session['student_id'] = student.student_id
                    return redirect(reverse('dashboard'))
                else:
                    form.add_error(None, "Invalid credentials.")
            except Student.DoesNotExist:
                form.add_error(None, "Invalid credentials.")
    else:
        form = StudentLoginForm()

    return render(request, 'students/login.html', {'form': form})
    
def dashboard(request):
    """
    A simple dashboard for logged-in students.
    """
    student = None
    enrolled_courses = []
    if 'student_id' in request.session:
        try:
            student = Student.objects.get(student_id=request.session['student_id'])
            # Get the courses enrolled by the student
            enrolled_courses = student.courses.all()
        except Student.DoesNotExist:
            # Handle the case where the session has a bad ID
            pass
    
    context = {
        'student': student,
        'enrolled_courses': enrolled_courses,
    }
    
    return render(request, 'students/dashboard.html', context)
    
def course_list(request):
    """
    A view to display all available courses.
    """
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'students/course_list.html', context)

def enroll_course(request):
    """
    A view to handle course enrollment.
    """
    if request.method == 'POST':
        # Get the course_code from the form
        course_code = request.POST.get('course_code')
        
        # Check if a student is logged in
        if 'student_id' in request.session:
            student_id = request.session['student_id']
            try:
                # Get the student and the course objects
                student = get_object_or_404(Student, student_id=student_id)
                course = get_object_or_404(Course, course_code=course_code)
                
                # Add the course to the student's courses
                student.courses.add(course)
                return redirect(reverse('dashboard'))
            except (Student.DoesNotExist, Course.DoesNotExist):
                # Handle cases where the student or course is not found
                pass
    
    return redirect(reverse('course_list'))

def logout_student(request):
    """
    A view to handle student logout.
    """
    if 'student_id' in request.session:
        del request.session['student_id']
    return redirect(reverse('login_student'))

def edit_profile(request):
    """
    A view to handle editing a student's profile.
    """
    if 'student_id' not in request.session:
        return redirect(reverse('login_student'))

    student = get_object_or_404(Student, student_id=request.session['student_id'])

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))
    else:
        form = StudentProfileForm(instance=student)
    
    context = {
        'form': form
    }
    return render(request, 'students/edit_profile.html', context)

def course_detail(request, course_code):
    """
    A view to display details for a single course, including enrolled students.
    """
    course = get_object_or_404(Course, course_code=course_code)
    enrolled_students = course.students.all()
    
    context = {
        'course': course,
        'enrolled_students': enrolled_students,
    }
    return render(request, 'students/course_detail.html', context)

def delete_enrollment(request, course_code):
    """
    A view to handle the deletion of a student's course enrollment.
    """
    if 'student_id' not in request.session:
        return redirect(reverse('login_student'))
    
    if request.method == 'POST':
        student = get_object_or_404(Student, student_id=request.session['student_id'])
        course = get_object_or_404(Course, course_code=course_code)
        
        # Remove the course from the student's enrolled courses.
        student.courses.remove(course)
    
    return redirect(reverse('dashboard'))
