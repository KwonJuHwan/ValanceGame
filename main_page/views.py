from django.shortcuts import render

from VSgames.models import Post


# Create your views here.
def main(request):
    post_list = Post.objects.all().order_by("-vote_sum").distinct()[:3]
    context={
        'post':post_list,
    }
    return render(request, 'main_page/main.html',context)
# def hot_page(request):
#     post_list = Post.objects.all().order_by("-vote_sum").distinct()
#     votes = Vote.objects.all()
#     tags = Tag.objects.all()
#     context = {
#         'post_list': post_list,
#         'votes': votes,
#         'tags': tags,
#     }
#     return render(request, 'VSgames/post_list.html', context)

