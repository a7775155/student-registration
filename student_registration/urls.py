# student_registration/urls.py

from django.contrib import admin
from django.urls import path, include
from student_registration import views # This line imports the views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('students/', include('students.urls')),
]
