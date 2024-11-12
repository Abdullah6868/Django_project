from rest_framework import serializers
from models import *



class StudentSerializer(serializers.Serializer):
    registration_no =  serializers.CharField (max_length = 20, unique=True, requeired = True)
    email =  serializers.EmailField (unique=True)