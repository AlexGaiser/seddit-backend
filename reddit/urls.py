from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main),
    path('reddit/post', views.RedditListCreate.as_view()),
    path('reddit/subreddit=<search>', views.Subreddit),
    path('reddit/search=<search>', views.RedditSearch),
    path('reddit/getsublist', views.subreddit_list)
]