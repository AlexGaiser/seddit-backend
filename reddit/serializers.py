from rest_framework import serializers
from reddit.models import RedditPosts


class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditPosts
        fields = '__all__'
