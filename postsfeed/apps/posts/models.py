from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('title', max_length = 50)
    content = models.TextField('content')
    publication_date = models.DateTimeField('publication_date', auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author_name = models.CharField('author_name', max_length = 50)
    text = models.CharField('text', max_length = 200)
    publication_date = models.DateTimeField('publication_date', auto_now = True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'