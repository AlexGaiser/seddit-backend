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

# class RedditListCreate(generics.ListCreateAPIView):
#     queryset = RedditPosts.objects.filter(karma__gte = 10000)[:10]
#     serializer_class = RedditSerializer
   

def startpage(request):
    return HttpResponse("Hello, world.This means that everything is working")

def dbpage(request):
   
    
    
    return HttpResponse("database is running.")
    # return HttpResponse("Hello, world.This means that everything is working")