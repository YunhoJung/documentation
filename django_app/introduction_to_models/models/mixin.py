'''
Post 모델
    author = User와 연결
    comments = MTM으로 Comment와 연결
    title
    content
    created_date
    modified_date

Comment 모델
    post = Post와 연결
    author = User와 연결
    content
    created_date
    modified_date

User 모델
    name
    created_date
    modified_date
'''

from django.db import models
from utils.models.mixins import TimeStampedMixin


class Post(TimeStampedMixin):
    author = models.ForeignKey('User')
    title = models.CharField(max_length=50)
    content = models.TextField()


class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey('User')
    content = models.TextField()


class User(TimeStampedMixin):
    name = models.CharField(max_length=50)

'''
PostLike
    Post = Post
    user = User
    create_date
    
Tag
    title
    
    
Post 모델
    like_users = User와 MTM으로 연결 Intermediate model로 PostLike모델을 사용
'''