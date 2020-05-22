from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('title', max_length = 50)
    content = models.TextField('content')
    post_publication_date = models.DateTimeField('post_publication_date')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author_name = models.CharField('author_name', max_length = 50)
    comment_text = models.CharField('comment_text', max_length = 200)
    comment_publication_date = models.DateTimeField('comment_publication_date')

    def __str__(self):
        return self.author_name