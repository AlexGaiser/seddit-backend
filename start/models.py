from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class RedditPosts(models.Model):
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
        managed = False
        db_table = 'reddit_posts'