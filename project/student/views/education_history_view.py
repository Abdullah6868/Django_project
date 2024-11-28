from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..models import EducationHistory, Student
from rest_framework import status
from rest_framework.views import APIView
from ..Serializer.education_history_serializer import EducationHistorySerializer
import json

class EductionHistoryView(APIView):
    def post(self , request , s_id):
        try:
            student = Student.objects.get(id = s_id)
        except Student.DoesNotExist:
            return JsonResponse({'Message': 'No Student Found!' }, status = status.HTTP_404_NOT_FOUND)

        data = json.loads(request.body)
        # # Check if a record for this student already exists
        # existing_record = EducationHistory.objects.filter(student=student).first()
        # if existing_record:
        #     return JsonResponse({"error": "Education data already exists for this student. Update the record instead."}, status=status.HTTP_400_BAD_REQUEST)
      
        data['student'] = student.id
        serializer = EducationHistorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Eduction data is added successfully.'})
        else:
            return JsonResponse({"errors": serializer.errors} , status = status.HTTP_400_BAD_REQUEST)
        

    def get(self , request , s_id = None , e_id = None):
        if s_id and e_id:
            try: 
                student  = EducationHistory.objects.get(id = e_id , student_id = s_id)
                
                serializer = EducationHistorySerializer(student)
                return JsonResponse(serializer.data , safe= False , status = status.HTTP_200_OK)
            except EducationHistory.DoesNotExist:
                return JsonResponse({"error": "Education history not found!"}, status = status.HTTP_404_NOT_FOUND)
        else:
           return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self , request , s_id , e_id):
        try: 
            update_education = EducationHistory.objects.get(id = e_id , student_id = s_id)
        except EducationHistory.DoesNotExist:
            return JsonResponse({"error": "Student not found!"} , status = status.HTTP_404_NOT_FOUND)
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid json data"}, status =status.HTTP_400_BAD_REQUEST)

        serializer = EducationHistorySerializer(update_education , data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'meassage': 'Education history updated successfully', 'data':serializer.data }, status = status.HTTP_200_OK)
        return JsonResponse(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request , e_id  , s_id):
        try:
            delete_education_history = EducationHistory.objects.get(id = e_id , student_id = s_id)
        except EducationHistory.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status =status.HTTP_404_NOT_FOUND)
        delete_education_history.delete()
        return JsonResponse({'message': 'Student Education history deleted successfully'}, status =status.HTTP_200_OK)
