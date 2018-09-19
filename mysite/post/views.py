from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
def post_list(request):
	
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	args={'posts': posts}
	
	return render(request, 'post/post_list.html', args)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_details.html', {'post': post})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post/add_comment_to_post.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

 
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def like_post(request):
    post = get_object_or_404(Post,id=request.Post.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes=add(request.user)
        is_liked = True
    context={
    'post':post,
    'is_liked':is_liked,
    'total_likes':post.total_likes
    }    
    if request.is_ajax():
        html=render_to_string('post/likes.html',context,request=request)
        return JsonResponse({'form':html})