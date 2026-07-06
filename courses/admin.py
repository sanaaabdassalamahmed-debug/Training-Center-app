from django.contrib import admin
from .models import Course,Trainer,Student,Enrollment

admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(Student)
admin.site.register(Enrollment)

