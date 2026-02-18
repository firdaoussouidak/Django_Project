from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author_id', 'author_username', 'date', 'comments_count')
        read_only_fields = ('id', 'author_id', 'author_username', 'date')

class CommentSerializer(serializers.ModelSerializer):
    is_author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'post_id', 'content', 'author_id', 'author_username', 'created_at', 'updated_at', 'is_author')
        read_only_fields = ('id', 'author_id', 'author_username', 'created_at', 'updated_at', 'is_author')

    def get_is_author(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.author_id == request.user.id
        return False


class CommentDetailSerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(source='post.title', read_only=True)
    is_author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'post_id', 'post_title', 'content', 'author_id', 'author_username', 'created_at', 'updated_at', 'is_author')
        read_only_fields = ('id', 'author_id', 'author_username', 'created_at', 'updated_at', 'post_title', 'is_author')

    def get_is_author(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.author_id == request.user.id
        return False


