from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm


class FeaturedPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')[:3]
    template_name = 'index.html'

class SpecificPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.order_by('-date_created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            'specific_post.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'comment': CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.order_by('-date_created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        return render(
            request, 
            'specific_post.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'comment': CommentForm()
            },
        )

class AllPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True).order_by('-date_created')
    template_name = 'blog.html'

class 