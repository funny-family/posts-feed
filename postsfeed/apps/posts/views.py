from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def posts(request):
    sortedPostsByPublicationDate = Post.objects.order_by('-post_publication_date')[:5]
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

    return render(request, 'posts/specifiedPost.html', {
        'post': receivedPost
    })