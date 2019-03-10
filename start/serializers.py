from rest_framework import serializers
from start.models import Lead, RedditPosts
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')


class RedditSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditPosts
        fields = '__all__'