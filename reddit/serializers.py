from rest_framework import serializers
from reddit.models import RedditPost


class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditPost
        fields = '__all__'
