from rest_framework import serializers
from django.conf import settings
from .models import Post, Category, Reply

#Post Category
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id','title','color','slug')

#Post
class PostSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField()
    category_title = serializers.ReadOnlyField()
    category_slug = serializers.ReadOnlyField()
    category_color = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('id', 'slug','status','title', 'text','category','created_date','user','owner_username','category_title','category_slug','category_color')

#Post Replies
class ReplySerializer(serializers.ModelSerializer):

    post_id = serializers.IntegerField(required=True)
    owner_username = serializers.ReadOnlyField()

    class Meta:
        model = Reply
        fields = ('id', 'text', 'created_date','user','post_id','owner_username')