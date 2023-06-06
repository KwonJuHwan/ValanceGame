import vote as vote
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from VSgames.forms import CommentForm
from VSgames.models import Post, Tag, Vote, User


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['tags'] = Tag.objects.all()
        context['votes'] = Vote.objects.all()
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['tags'] = Tag.objects.all()
        context['comment_form'] = CommentForm
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['first_question', 'second_question', 'summary', 'tag']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCreate, self).get_context_data()
        context['tags'] = Tag.objects.all()
        return context

    def form_valid(self, form):
        # 로그인이 되어있다면
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/')


class UserDetail(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data()
        context['tags'] = Tag.objects.all()
        return context


def tag_page(request, slug):
    # MtoM 이기 때문에, 다음과 같이 설정해야함
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all().order_by('-pk')

    # FBV  특징
    context = {
        'tag': tag,
        'post_list': post_list,

    }
    return render(request, 'VSgames/post_list.html', context)


def post_page(request, pk):
    author = User.objects.get(pk=pk)
    post_list = author.post_set.all().order_by('-pk')
    votes = Vote.objects.all()
    tags= Tag.objects.all()
    context = {
        'usedUser': author,
        'post_list': post_list,
        'votes': votes,
        'tags': tags,
    }
    return render(request, 'VSgames/post_list.html', context)


def add_comment(request, pk):
    if not request.user.is_authenticated:
        raise PermissionError

    # pk를 통해, Post 찾기 for Redirect
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        # DB 에 넣기 전 필요한 field 를 채우기 위해 temp 생성
        comment_temp = comment_form.save(commit=False)
        comment_temp.post = post
        comment_temp.author = request.user
        # DB 에 넣기
        comment_temp.save()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionError


class VoteDetail(DetailView):
    model = Post
    template_name = 'VSgames/vote_detail.html'

    def get_context_data(self, **kwargs):
        context = super(VoteDetail, self).get_context_data()
        context['tags'] = Tag.objects.all()
        return context


def add_vote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        votes = Vote.objects.filter(post=post)
        voted = False
        for anyVote in votes:
            if anyVote.author == request.user:
                voted = True
                question = request.POST['question']
                if anyVote.choice == post.first_question:
                    post.first_sum -= 1
                elif anyVote.choice == post.second_question:
                    post.second_sum -= 1
                post.save()
                anyVote.delete()
        question = request.POST['question']
        vote = Vote()
        vote.post = post
        vote.author = request.user
        vote.choice = question
        if question == post.first_question:
            post.first_sum += 1
        elif question == post.second_question:
            post.second_sum += 1
        post.save()
        vote.save()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionError


def hot_page(request):
    post_list = Post.objects.all().order_by("-vote")
    votes = Vote.objects.all()
    tags = Tag.objects.all()
    context = {
        'post_list': post_list,
        'votes': votes,
        'tags': tags,
    }
    return render(request, 'VSgames/post_list.html', context)


def delete_post(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect("/")