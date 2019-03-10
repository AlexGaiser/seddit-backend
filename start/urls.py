from django.urls import path

from . import views

urlpatterns = [
    path('', views.LeadListCreate.as_view(), name='index'),
    path('db', views.dbpage),
    path('reddit', views.RedditListCreate.as_view())
]