from django.db import models

class RedditPost(models.Model):
    post_id = models.CharField(unique=True, max_length=6, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)
    subreddit = models.CharField(max_length=500, blank=True, null=True)
    submission_link_url = models.CharField(max_length=1000, blank=True, null=True)
    submission_url = models.CharField(max_length=1000, blank=True, null=True)
    date_time = models.CharField(max_length=100, blank=True, null=True)
    collected_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'reddit_posts'

# class RedditPostsHot(models.Model):
#     post_id = models.CharField(unique=True, max_length=6, blank=True, null=True)
#     title = models.CharField(max_length=1000, blank=True, null=True)
#     body = models.TextField(blank=True, null=True)
#     karma = models.IntegerField(blank=True, null=True)
#     subreddit = models.CharField(max_length=500, blank=True, null=True)
#     submission_link_url = models.CharField(max_length=1000, blank=True, null=True)
#     submission_url = models.CharField(max_length=1000, blank=True, null=True)
#     date_time = models.CharField(max_length=100, blank=True, null=True)
#     collected_date = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'reddit_posts_hot'

# # class NlpSentimentTitle(models.Model):
# #     post_id = models.CharField(unique=True, max_length=6, blank=True, null=True)
# #     sentiment_polarity = models.IntegerField(blank=True, null=True)
# #     sentiment_subjectivity = models.CharField(max_length=-1, blank=True, null=True)
# #     title = models.TextField(blank=True, null=True)
# #     class Meta:
# #         managed = False
# #         db_table = 'nlp_sentiment_title'



# class RedditPostsNew(models.Model):
#     post_id = models.CharField(unique=True, max_length=6, blank=True, null=True)
#     title = models.CharField(max_length=1000, blank=True, null=True)
#     body = models.TextField(blank=True, null=True)
#     karma = models.IntegerField(blank=True, null=True)
#     subreddit = models.CharField(max_length=500, blank=True, null=True)
#     submission_link_url = models.CharField(max_length=1000, blank=True, null=True)
#     submission_url = models.CharField(max_length=1000, blank=True, null=True)
#     date_time = models.CharField(max_length=100, blank=True, null=True)
#     collected_date = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'reddit_posts_new'

# class RedditPostsRising(models.Model):
#     post_id = models.CharField(unique=True, max_length=6, blank=True, null=True)
#     title = models.CharField(max_length=1000, blank=True, null=True)
#     body = models.TextField(blank=True, null=True)
#     karma = models.IntegerField(blank=True, null=True)
#     subreddit = models.CharField(max_length=500, blank=True, null=True)
#     submission_link_url = models.CharField(max_length=1000, blank=True, null=True)
#     submission_url = models.CharField(max_length=1000, blank=True, null=True)
#     date_time = models.CharField(max_length=100, blank=True, null=True)
#     collected_date = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'reddit_posts_rising'


