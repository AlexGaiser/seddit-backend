from rest_framework import serializers
from reddit.models import RedditPostsHot


class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditPostsHot
        fields = '__all__'
