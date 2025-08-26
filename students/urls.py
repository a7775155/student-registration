# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
      path('login/', views.login_student, name='login_student'), # New URL for login
      path('dashboard/', views.dashboard, name='dashboard'), # New URL for the dashboard 
       path('courses/', views.course_list, name='course_list'), # This is the new URL
       path('enroll/', views.enroll_course, name='enroll_course'), # This is the new URL
        path('logout/', views.logout_student, name='logout_student'), # New URL for logout
        path('profile/edit/', views.edit_profile, name='edit_profile'), # New URL
         path('courses/<str:course_code>/', views.course_detail, name='course_detail'), # New URL
          path('delete_enrollment/<str:course_code>/', views.delete_enrollment, name='delete_enrollment'), # New URL
]
