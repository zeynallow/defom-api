from rest_framework import serializers
from django.conf import settings
from .models import Post, Category, Tag, Reply

#Post Category
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id','title')

#Post Tag
class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id','title')

#Post
class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    tags = serializers.StringRelatedField(many=True)
    owner_username = serializers.ReadOnlyField()
    

    class Meta:
        model = Post
        fields = ('id', 'slug','status','title', 'text','categories','tags','created_date','user','owner_username')

#Post Replies
class ReplySerializer(serializers.ModelSerializer):

    post_id = serializers.IntegerField(required=True)
    owner_username = serializers.ReadOnlyField()

    class Meta:
        model = Reply
        fields = ('id', 'text', 'created_date','user','post_id','owner_username')