from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import sqlalchemy

from reddit.models import RedditPostsHot, RedditPosts
from reddit.serializers import RedditSerializer
from rest_framework import generics
# import cfg, schema, nlp_script, insert_pgdb, geddit
# from reddit.collection_app import geddit, nlp_script
from django.contrib.postgres.search import SearchVector


# class RedditListCreate(generics.ListCreateAPIView):
#     queryset = RedditPostsHot.objects.filter(karma__gte = 10000)[:10]
#     serializer_class = RedditSerializer
    

def Main(request):
    # qs = RedditPosts.objects.order_by('-collected_date')[:20]
    # qs = list(qs.values())

    # return JsonResponse({'data':qs}, safe = False)
    return HttpResponse("Hello, world.This means that everything is working")


# def subreddit_list(request):
#     print('fetching reddit list')

#     posts = RedditPosts.objects.order_by('subreddit').distinct("subreddit")
    
#     posts = list(posts.values())
#     return JsonResponse({
#             "count":len(posts),
#             "posts": posts})

# def Subreddit(request, search):
#     try:
#         posts = RedditPosts.objects.filter(subreddit__iexact=str(search))
#     except:
#         pass
    
#     geddit.get_reddit_data(subreddit=search, sort="hot", limit=50) 
        
#     if len(posts)<300:
#         geddit.get_reddit_data(subreddit=search, sort="top", filter='all', limit=1000)

#     posts = RedditPosts.objects.filter(subreddit__iexact=str(search))
    
#     if len(posts) >=300:
#         sentiment = nlp_script.sentiment(posts, search)
#         posts = list(posts.values())
        
#         return JsonResponse({
#             "count":len(posts),
#             "sentiment": sentiment})
#             # 'data':posts}, safe = False)
#     else:

#         sentiment = {"polarity": 0, "subjectivity": 0}

#         return JsonResponse({
#             "count":len(posts),
#             "sentiment": sentiment,
#             "message": "insufficient data for analysis"
#         })

# def RedditSearch(request, search):
#     results = RedditPosts.objects.annotate(search=SearchVector('title', 'body'),).filter(search=search)
    
#     if len(results)< 200:
#         print('starting search')
#         geddit.reddit_search(search)
    
#     results = RedditPosts.objects.annotate(search=SearchVector('title', 'body'),).filter(search=search)
    
#     sentiment = nlp_script.sentiment(results, search.lower())
    
#     results = list(results.values())

#     return JsonResponse({
#             "count":len(results),
#             "sentiment": sentiment,
#             "data": results
#             })



# def GetRedditData(request):
#     geddit.get_reddit_data(subreddit="all", sort="new", limit=1000)
#     geddit.get_reddit_data(subreddit="all", sort="rising", limit=1000)
#     geddit.get_reddit_data(subreddit="all", sort="controversial", limit=1000)    
#     geddit.get_reddit_data(subreddit="all", sort="hot", limit=1000) 
    
#     return JsonResponse({'message':'datacollected'})
