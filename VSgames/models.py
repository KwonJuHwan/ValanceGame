from django.db import models


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
    #  vote_sum 얼마나 많은 사람들이 투표 했는지
    #  comment 댓글
    # like 좋아요
    # first_sum 첫번째 투표 수
    # second_sum 두번째 투표 수

    # 작성자와 태그 관계 형성하기

    def __str__(self):
        return f'[{self.pk}]{self.first_question} VS {self.second_question}'

    def get_absolute_url(self):
        return f'/{self.pk}'