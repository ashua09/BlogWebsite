from pyexpat import model
from tokenize import blank_re
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, ImageField
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):

    name=models.CharField(max_length=200) 
    
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("blog:home")

class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    header_image=models.ImageField(null=True, blank=True,upload_to='images/')
    body=RichTextField(blank=True,null=True)
    # body=models.TextField()
    published_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255)
    snippet=models.CharField(max_length=255,default="Here You write the little intro for blog")
    # likes=models.ManyToManyField(User, related_name='blog_posts')       #Related_name work as a foreign key

    # def total_likes(self):
    #     return self.likes.count()

    def __str__(self):
        return f'{self.title} is written by {self.author}'

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})

class Profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True, blank=True,upload_to='images/profile/')
    website_url=models.CharField(max_length=200,null=True, blank=True)
    facebook_url=models.CharField(max_length=200,null=True, blank=True)
    insta_url=models.CharField(max_length=200,null=True, blank=True)
    linkdin_url=models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse("blog:home")

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} comment by {self.name}'
























# Code for like and unlike in .html
# <form action="{% url 'blog:like_post' post.pk %}" method="POST">
#     {% csrf_token %}

#     {% if liked %}
#         <button type="submit" class="btn btn-danger btn-sm",name='post_id',value='{{post.id}}'>Unlike</button>
#     {% else %}
#         <button type="submit" class="btn btn-primary btn-sm",name='post_id',value='{{post.id}}'>Like</button>
#     {% endif %}
        
#     -{{total_likes}} Likes
# </form>
