from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from start.models import Lead
from start.serializers import LeadSerializer
from rest_framework import generics
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


def startpage(request):
    return HttpResponse("Hello, world.This means that everything is working")

