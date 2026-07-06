from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Trainer, Student, Enrollment
from .serializers import (
    CourseSerializer,
    TrainerSerializer,
    StudentSerializer,
    EnrollmentSerializer
)

# ================= COURSES =================

@api_view(['GET', 'POST'])
def courses(request):

    if request.method == 'GET':
        data = Course.objects.all()
        serializer = CourseSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['DELETE'])
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return Response({"message": "Deleted"})


# ================= STUDENTS =================

@api_view(['GET', 'POST'])
def students(request):

    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['DELETE'])
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"message": "Deleted"})


# ================= TRAINERS =================

@api_view(['GET', 'POST'])
def trainers(request):

    if request.method == 'GET':
        data = Trainer.objects.all()
        serializer = TrainerSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrainerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(['DELETE'])
def delete_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return Response({"message": "Deleted"})


# ================= ENROLL =================

@api_view(['POST'])
def enroll_student(request):

    student = Student.objects.get(id=request.data['student_id'])
    course = Course.objects.get(id=request.data['course_id'])

    enrollment = Enrollment.objects.create(
        student=student,
        course=course
    )

    return Response(EnrollmentSerializer(enrollment).data)