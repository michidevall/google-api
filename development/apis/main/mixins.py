from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json
import datetime
from humanfriendly import format_timespan
from django.http import JsonResponse

def FormErrors(*args):
    
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message

def reCAPTHCHAValidation(token):
    
    result = requests.post(
        
    )