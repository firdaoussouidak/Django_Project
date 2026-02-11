from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author_id', 'author_username', 'date')
        read_only_fields = ('id', 'author_id', 'author_username','date')
