from django.urls import path
from .views import *

urlpatterns = [

    # COURSES
    path('courses/', courses),
    path('courses/<int:id>/', delete_course),

    # STUDENTS
    path('students/', students),
    path('students/<int:id>/', delete_student),

    # TRAINERS
    path('trainers/', trainers),
    path('trainers/<int:id>/', delete_trainer),

    # ENROLL
    path('enroll/', enroll_student),
]