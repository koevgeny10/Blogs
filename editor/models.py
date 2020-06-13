from django.db import models
from django.urls import reverse
from blogs.models import Blog


class Article(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='articles',
        related_query_name='article'
    )
    name = models.TextField(unique=True, help_text='please be short')
    text = models.TextField(null=True)
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)
    moment = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'moment'
        ordering = ['moment']

    def __str__(self):
        return f'{self.name} from {self.blog.name}'

    def get_absolute_url(self):
        return reverse(
            'blogs:article:article',
            kwargs={'blog_id': self.blog.id, 'article_id': self.id}
        )
