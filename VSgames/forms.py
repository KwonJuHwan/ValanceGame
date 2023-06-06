from .models import Comment, Vote
from django import forms


# 댓글 form
# view를 하나 만드는 것이 아닌 view 안으로 넣어야 되기 때문에 따로 form 으로 만든 것
# View(PostDetail) 안에 form 을 넣을꺼 ->forms.ModelForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 어떤 값들을 받아낼 것인지
        fields = ('content',)


