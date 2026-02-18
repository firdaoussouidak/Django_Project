from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, CommentDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Post, Comment


class PostCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                author_id=request.user.id,
                author_username=request.user.username
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        posts = Post.objects.all().order_by('-date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyPostListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        posts = Post.objects.filter(author_id=request.user.id).order_by('-date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,post_id):
        try:
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class PostDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self,request,post_id):
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PostUpdateView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self,request,post_id):
        try:
            post = Post.objects.get(id=post_id)
            serializer = PostSerializer(post, request.data,  partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                post=post,
                author_id=request.user.id,
                author_username=request.user.username)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)  # ← Correction: post, pas posts
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        comments = Comment.objects.filter(post_id=post_id).order_by('-created_at')  # ← created_at
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            serializer = CommentDetailSerializer(comment, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentUpdateView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self,request,comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(comment, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self,request,comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyCommentListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        comments = Comment.objects.filter(author_id=request.user.id).order_by('-created_at')
        serializer = CommentDetailSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailWithCommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request,post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post_serializer = PostSerializer(post)
        comments = Comment.objects.filter(post=post).order_by('-created_at')
        comment_serializer = CommentSerializer(comments, many=True, context={'request': request})

        data = post_serializer.data
        data['comments'] = comment_serializer.data
        data['comments_count'] = comments.count()

        return Response(data, status=status.HTTP_200_OK)
