# from typing import Any
from django.http import HttpResponseForbidden


ALLOWED_IPS = ['127.0.0.1', '192.168.100.40']

class Restrictip:
    
    def __init__(self , get_response):
        self.get_response = get_response

    def __call__(self, request) :
        if request.META.get('REMOTE_ADDR') not in ALLOWED_IPS:
            return HttpResponseForbidden("Access Denied")
        return self.get_response(request)
