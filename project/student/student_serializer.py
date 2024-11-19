from rest_framework import serializers
from .models import Student
from django.utils import timezone



class StudentSerializer(serializers.Serializer):
    name =  serializers.CharField(max_length=100,required=True)
    registration_no =  serializers.CharField (max_length = 20,required=True)
    email =  serializers.EmailField (required=False, allow_blank = True)
    room_no  = serializers.IntegerField(required=True)
    section_choice = [
        ("A","A"),
        ("B","B"),
        ("C","C"),
    ]
    section = serializers.CharField(max_length = 1,required=True)
    class Meta:
        model = Student
        fields = ['name','registration_no','email','room_no','section','updated_at'] # or '__all__
        read_only_fields = ['created_at']
    
    def validate_name(self, value):
        # Check if the name is not blank or empty
        if not value or not value.strip():
            raise serializers.ValidationError("Name cannot be blank.")
        return value
    def validate_registration_no(self , value):
        if Student.objects.filter(registration_no = value).exists():
            raise serializers.ValidationError("Registration number is already exist.")
        return value
    def validate_email(self , value):
        if Student.objects.filter(email = value).exists():
            raise serializers.ValidationError("Email already exist.")
        return value
    def validate_room_no(self , value):
        if value <=0:
            raise serializers.ValidationError("Room number should be greater than zero.")
        return value
    def validate_section(self , value):
        if value not in dict(self.section_choice):
            raise serializers.ValidationError("Sections value must be one of 'A', 'B' or 'C' ")
        return value
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.registration_no = validated_data.get('registration_no', instance.registration_no)
        instance.email = validated_data.get('email', instance.email)
        instance.room_no = validated_data.get('room_no', instance.room_no)
        instance.section = validated_data.get('section', instance.section)
        instance.updated_at = timezone.now()
        instance.save()
        return instance