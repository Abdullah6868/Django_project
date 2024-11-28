from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..models import Certificate, Student
from rest_framework import status
from rest_framework.views import APIView
from ..Serializer.certificate_serializer import CertificateSerializer
import json

class CertificateView(APIView):
    def post(self, request, s_id):
        try:
            student = Student.objects.get(id=s_id)
        except Student.DoesNotExist:
            return JsonResponse({'Message': 'Student not found!'})
        # Prepare data from request
        data = request.data.copy()
        uploaded_file = request.FILES.get('certificate_file')  # Safely get the uploaded file

        # If a file is uploaded, add it to the data dictionary
        if uploaded_file:
            data['certificate_file'] = uploaded_file

        data['student'] = student.id

        # Prepare serializer
        serializer = CertificateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({'message': 'Certificate data is added successfully.'})

        return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, s_id, c_id):
        if s_id and c_id:
            try: 
                student  = Certificate.objects.get(id = c_id , student_id = s_id)
                serializer = CertificateSerializer(student)
                return JsonResponse(serializer.data , safe= False , status = status.HTTP_200_OK)
            except Certificate.DoesNotExist:
                 return JsonResponse({"error": "Certificates not found!"}, status = status.HTTP_404_NOT_FOUND)

    def put(self, request, s_id , c_id):
        try:
            update_certificate = Certificate.objects.get(id = c_id , student_id = s_id)

        except Certificate.DoesNotExist:
            return JsonResponse({'Message': 'Certificate Record not found'}, status =status.HTTP_404_NOT_FOUND)
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid json data '}, status = status.HTTP_400_BAD_REQUEST)

        serializer = CertificateSerializer(update_certificate , data = data , partial =True)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse({'message': 'Certificate data updated successfully' , 'data': serializer.data}, status = status.HTTP_200_OK )
        return JsonResponse(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    
    def delete(self , request , c_id  , s_id ):
        try:
             delete_student_certificate = Certificate.objects.get(id = c_id , student_id = s_id)
             delete_student_certificate.delete()
             return JsonResponse({'Message': 'Student Certificate data is deleted successfully'}, status= status.HTTP_200_OK)
        except Certificate.DoesNotExist:
            return JsonResponse({'Message': 'Certificate Record not found'}, status = status.HTTP_400_BAD_REQUEST)
        
       
    