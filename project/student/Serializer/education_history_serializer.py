from rest_framework import serializers
from ..models import  EducationHistory
from datetime import date
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from ..models import EducationHistory, Student

class EducationHistorySerializer(serializers.ModelSerializer):

    institution_name  = serializers.CharField(max_length=200 , required = True)
    degree = serializers.CharField(max_length=100 ,  required = True)
    field_of_study  = serializers.CharField(max_length=100 ,  required = True)
    start_date =  serializers.DateField(required = True)
    end_date   = serializers.DateField()
    grade  = serializers.CharField(max_length=10, required = True)

    class Meta:
        model = EducationHistory
        fields =  '__all__'
    
    def validate_institution_name(self, value):
        if not value or not value.strip():
            return serializers.ValidationError("Institute name cannot be blank!")
        return value
    def validate_degree(self, value):
        student = self.initial_data.get("student") 
        if EducationHistory.objects.filter(student=student, degree=value).exists():
            raise serializers.ValidationError("This degree is already exists for this student.")
        if not value or not value.strip():
            return serializers.ValidationError("Degree field cannot be blank!")
        return value
    def validate_field_of_study(self, value):
        student = self.initial_data.get("student") 
        if EducationHistory.objects.filter(student=student, field_of_study=value).exists():
            raise serializers.ValidationError("This field is already exists for this student.")
        
        if not value or not value.strip():
            return serializers.ValidationError("Field of study cannot be blank!")
        return value
    
    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        if start_date and  end_date and end_date < start_date:
            raise serializers.ValidationError("End date cannot be earlier than start date")
        if start_date and not isinstance(start_date , date):
            raise serializers.ValidationError("Invalid date format for start_date. Expected YYYY-MM-DD.")
        if end_date and not isinstance(end_date,date):
            raise serializers.ValidationError("Invalid date format for end_date. Expected YYYY-MM-DD.")
        return data
    
    def create(self, validated_data):
        return EducationHistory.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance , validated_data)
