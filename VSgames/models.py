from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/tag/{self.slug}/'


class User(AbstractUser):
    nickname = models.CharField(max_length=50)


class Post(models.Model):
    # 첫번째 vs
    first_question = models.CharField(max_length=30)
    # 두번째 vs
    second_question = models.CharField(max_length=30)
    # 한줄 설명
    summary = models.TextField()
    # 작성 일자
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # first_sum 첫번째 투표 수
    first_sum = models.IntegerField(default=0)
    # second_sum 두번째 투표 수
    second_sum = models.IntegerField(default=0)
    #  vote_sum 얼마나 많은 사람들이 투표 했는지

    # 작성자와 태그 관계 형성하기
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.first_question} VS {self.second_question}'

    def get_absolute_url(self):
        return f'/{self.pk}'

    def get_total_vote(self):
        sum = self.first_sum + self.second_sum
        return sum

    def get_per_first_vote(self):
        sum = self.first_sum + self.second_sum
        ask = self.first_sum / sum
        ask = ask * 100
        return round(ask, 2)

    def get_per_second_vote(self):
        sum = self.first_sum + self.second_sum
        ask = self.second_sum / sum
        ask = ask * 100
        return round(ask, 2)


class Comment(models.Model):
    # 어떤 글에 대한 댓글 인가
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 누가 썼는가
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 어떤 내용
    content = models.TextField()
    # 언제 썼는가
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 가능 한가? 가능 하다면 언제 수정 했는가?
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    # comment 로 가기 위한 링크 메소드
    # comment 가 달린 페이지 -> self.post.get_absolute_url()
    # 페이지 중 댓글이 달린 곳으로 이동(앵커) -> #comment-{self.pk}
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice = models.TextField(default="null")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}::{self.post}::{self.choice}'
