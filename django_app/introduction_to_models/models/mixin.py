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
    # 이 Post에 좋아요를 누른 사람들
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        related_name='like_posts')

    # 중간자 모델쓰면 add 안됌. like_users가 through를 이용해서 PostLike를 Intermediate모델로 거쳐가도록 설정
    # m2m through를 하게되면 m2m으로 엮인 두 테이븖 사이에 새로 지정한 테이블이 중간 매니저 역할을 하게 된다
    # 중간자 모델(PostLike)을 사용해서 좋아요를 추가하면 하나의 테이블에 좋아요의 주체, 날짜에 관한 정보를 모두 저장할 수 있다.
    # 기존의 m2m의 경우에는 유저나 포스트, 한 쪽에서 추가했지만
    # 중간자 모델의 경우에는 하나에 누락된 정보를 모두 저장할 수 있다.
    # migrate showall
    # migrate 덮어씌울 파일 --fake (가장 최신으로 업데이트한다)

class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey('User')
    content = models.TextField()


class User(TimeStampedMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'introduction_to_models_post_like_users'


# class PostLike(models.Model):
#     post = models.ForeignKey(Post)
#     user = models.ForeignKey(User)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '{author}의 ({post_title})에 대한 {like_user}의 좋아요 ({like_datetime})'.format(
#             author=self.post.author.name,
#             post_title=self.post.title,
#             like_user=self.user.name,
#             like_datetime=self.created_date,
#         )
#
#     class Meta:
#         db_table = 'introduction_to_models_post_like_users'


# class Tag(models.Model):
#     title = models.CharField(max_length=50)


'''
1. PostLike, Tag모델 추가
2. Post모델에 like_users MTM필드 추가 및 through선언
3. makemigrations -> migrate 잘 되는지 확인
4. Django shell에서 Post의 like_users에 임의의 User추가하고 결과 확인

PostLike
    Post = Post
    user = User
    create_date
    
Tag
    title
    
    
Post 모델
    like_users = User와 MTM으로 연결 Intermediate model로 PostLike모델을 사용
    tags = MTM으로 Tag와 연결
    
    def like_post(self, user):
        return '해당 user의 PostLike를 생성 이후 생성 객체를 리턴'
    
    def add_tag(self, tag_name):
        return '해당 tag_name의 Tag를 생성 또는 기존항목 가져와서 Post에 추가, 이후 Tag리턴
'''
