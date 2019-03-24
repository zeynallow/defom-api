from rest_framework.generics import get_object_or_404
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Category, Tag, Reply
from .serializers import PostSerializer, CategorySerializer, TagSerializer, ReplySerializer

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

#Topic Post
class PostView(APIView):

    #Single Post
    def get(self, request, pk=None):
        if pk:
            post = get_object_or_404(Post.objects.all(), pk=pk)
            serializer = PostSerializer(post)
            return Response({"post": serializer.data})
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    #Create Post
    def post(self, request):
        if request.user.is_authenticated:
            # Create an post from the above data
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                post_saved = serializer.save(user_id = request.user.id)
                return Response({"success": "Post '{}' created successfully".format(post_saved.title)})
        else:
            return Response({"error": "Please login"})

    # def put(self, request, pk):
    #
    #     saved_post = get_object_or_404(Post.objects.all(), pk=pk)
    #     data = request.data.get('post')
    #     serializer = PostSerializer(instance=saved_post, data=data, partial=True)
    #
    #     if serializer.is_valid(raise_exception=True):
    #         post_saved = serializer.save()
    #     return Response({"success": "Post '{}' updated successfully".format(post_saved.title)})
    #
    #
    # def delete(self, request, pk):
    #     # Get object with this pk
    #     post = get_object_or_404(Post.objects.all(), pk=pk)
    #     post.delete()
    #     return Response({"message": "Post with id `{}` has been deleted.".format(pk)},status=204)


#Topic Category
class CategoryView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category.objects.all(), pk=pk)
            serializer = CategorySerializer(category)
            return Response({"category": serializer.data})
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories": serializer.data})



#Topic Tag
class TagList(APIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names = ['get', 'post', 'head']


class TagDetail(APIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names = ['get', 'post', 'head']


#Topic Replies
class ReplyView(APIView):
    
    #Get All Replies
    def get(self, request, pk=None):
            reply = get_list_or_404(Reply.objects.all(), post_id=pk)
            serializer = ReplySerializer(reply, many=True)    
            return Response({"replies": serializer.data})

    #Add Reply
    def post(self, request):
        if request.user.is_authenticated:
            serializer = ReplySerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user_id = request.user.id)
                return Response({"success": "Reply created successfully"})
        else:
            return Response({"error": "Please login"})