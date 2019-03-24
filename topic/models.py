from django.db import models
from django.conf import settings
from django.utils import timezone
from autoslug import AutoSlugField


#Topic Categories
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', null=True)
    color = models.CharField(max_length=200,null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


#Topic Posts
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, db_index=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    status = models.CharField(max_length=10, default='published')
    created_date = models.DateTimeField(default=timezone.now,db_index=True)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', null=True)


    def owner_username(self):
        return self.user.username

    def category_title(self):
        return self.category.title
    
    def category_color(self):
        return self.category.color

    def category_slug(self):
        return self.category.slug

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#Topic Replies
class Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, related_name='post',on_delete=models.CASCADE, null=True,db_index=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now,db_index=True)

    def owner_username(self):
        return self.user.username