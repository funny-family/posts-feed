from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def posts(request):
    sortedPostsByPublicationDate = Post.objects.order_by('-post_publication_date')
    return render(
        request,
        'posts/potsList.html',
        {
            'sortedPostsByPublicationDate': sortedPostsByPublicationDate
        }
    )

def specifiedPost(request, postId):
    try:
        receivedPost = Post.objects.get(id = postId)
    except:
        raise Http404('Post not found!')

    # comments = receivedPost.comment_set.order_by('-comment_publication_date')
    comments = receivedPost.comment_set.order_by('-id')

    return render(request, 'posts/specifiedPost.html', {
        'post': receivedPost,
        'comments': comments
    })

def leaveComment(request, postId):
    try:
        receivedPost = Post.objects.get(id = postId)
    except:
        raise Http404('Post not found!')

    receivedPost.comment_set.create(
        author_name = request.POST['author-name'], # author_name is a name from db
        comment_text = request.POST['comment'] # comment_text is a name from db
    )
    return HttpResponseRedirect(reverse('posts:specifiedPost', args = (receivedPost.id,)))