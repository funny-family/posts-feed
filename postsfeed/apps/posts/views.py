from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Post, Comment

# Create your views here.
def posts(request):
    sortedPostsByPublicationDate = Post.objects.order_by('-publication_date')
    return render(
        request,
        'posts/potsList.html',
        {
            'sortedPostsByPublicationDate': sortedPostsByPublicationDate
        }
    )

def specifiedPost(request, postId):
    try:
        specifiedPost = Post.objects.get(id = postId)
    except:
        raise Http404('Post not found!')

    comments = specifiedPost.comment_set.order_by('-publication_date')

    return render(request, 'posts/specifiedPost.html', {
        'post': specifiedPost,
        'comments': comments
    })

class PostCreateView(CreateView):
    model = Post
    success_url = '/' # redirect to '/'
    fields = [
        'title',
        'content',
        'author_name',
    ]

def leaveComment(request, postId):
    try:
        receivedPost = Post.objects.get(id = postId)
    except:
        raise Http404('Post not found!')

    receivedPost.comment_set.create(
        author_name = request.POST['author-name'], # author_name is a name from db
        text = request.POST['comment'] # text is a name from db
    )
    return HttpResponseRedirect(reverse('posts:specifiedPost', args = (receivedPost.id,)))