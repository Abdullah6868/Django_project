# student/views/student_view.py
from django.http import JsonResponse
from student.models import Student
from  ..Serializer.student_serializer import StudentSerializer 
from rest_framework import status
from rest_framework.views import APIView
import json


class StudentView(APIView):
    def post(self,request):
         try:
            data = json.loads(request.body)
            serializer = StudentSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Student data inserted successfully", "data": serializer.data})
            
            else:
                return JsonResponse({"errors": serializer.errors}, status=400)
         except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get(self, request , s_id = None):
        if s_id:
            try:
               student = Student.objects.get(id = s_id)
               serializer = StudentSerializer(student)
               return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
             return JsonResponse({'error':'Student not found.'}, status= status.HTTP_404_NOT_FOUND)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student , many = True)
            return JsonResponse(serializer.data , safe=False , status = status.HTTP_200_OK)

    def put(self,request, s_id):
         try:
            student_update = Student.objects.get(id = s_id)
         except Student.DoesNotExist:
                return JsonResponse({'errors':'Student not found'}, status = status.HTTP_404_NOT_FOUND)
        
         try:
            # Parse the JSON data
            data = json.loads(request.body)
         except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
        
         serializer  = StudentSerializer(student_update, data = data , partial = True )
         if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Student updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
            # return JsonResponse(serializer.data , status = status.HTTP_200_OK)
         return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , s_id):
        try:
            student_delete = Student.objects.get(id=s_id)
        except Student.DoesNotExist:
            return JsonResponse({'errors': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        student_delete.delete()
        return JsonResponse({'message': 'Student data deleted successfully'}, status=status.HTTP_200_OK)

