from django.shortcuts import render
from models import * 

# Create your views here.

def student(request):
    if(request.method == "POST"):
        data = request.POST
        name = data.get("name")
        registration_no = data.get("registration_no")
        email = data.get("email")
        room_no = data.get("room_no")
        section = data.get("section")
        created_at = data.get("created_at")
        updated_at = data.get("updated_at")
