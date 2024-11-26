from rest_framework import serializers
from ..models import  Certificate
from datetime import date
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from ..models import Certificate, Student                                                                                                                                                                                                                                                                                                                              


class CertificateSerializer(serializers.ModelSerializer):
    certificate_name = serializers.CharField(max_length=100 ,  required = True)
    issued_by  = serializers.CharField(max_length=100 ,  required = True)
    date_issued =  serializers.DateField(required = True)
    description   = serializers.CharField()
    certificate_file  = serializers.FileField(required = False , default = None)

    class Meta:
        model = Certificate
        fields =  '__all__'
    
    def validate_certificate_name(self, value):
        if not value or not value.strip():
            return serializers.ValidationError("Certificate name cannot be blank!")
        student = self.initial_data.get("student") 
        if Certificate.objects.filter(student=student, certificate_name=value).exists():
            raise serializers.ValidationError("A certificate with this name already exists for this student.")
        return value
    def validate_issued_by(self, value):
        if not value or not value.strip():
            return serializers.ValidationError("Issued by field cannot be blank!")
        return value
    def validate_date_issued(self, value):
        if not isinstance(value, date):
            raise serializers.ValidationError("'Message':  Invalid date format for date_issued. Expected YYYY-MM-DD.")
        return value
    
    def create(self, validated_data):
        return Certificate.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance , validated_data)
