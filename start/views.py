from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import os
from start.models import Lead
from start.serializers import LeadSerializer
from rest_framework import generics
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


def startpage(request):
    return HttpResponse("Hello, world.This means that everything is working")

def dbpage(request):
    if 'RDS_DB_NAME' in os.environ:
        DATABASES = {
                'DEPLOYED': 'Deployed',
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ['RDS_DB_NAME'],
                'USER': os.environ['RDS_USERNAME'],
                'PASSWORD': os.environ['RDS_PASSWORD'],
                'HOST': os.environ['RDS_HOSTNAME'],
                'PORT': os.environ['RDS_PORT'],
            }
    else:
        DATABASES = {
                'LOCAL': 'local',
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'django1',
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
        }
        
    
    return JsonResponse(DATABASES, safe=False)
    # return HttpResponse("Hello, world.This means that everything is working")