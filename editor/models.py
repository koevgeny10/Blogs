from django.db import models
from django.urls import reverse
from bloging.models import Blogs


class Articles(models.Model):
    blog = models.ForeignKey(
        Blogs,
        on_delete=models.CASCADE,
        to_field='name',
        related_name='articles',
        related_query_name='article'
    )
    name = models.TextField(primary_key=True, help_text='please be short')
    text = models.TextField(null=True)
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)
    moment = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'moment'
        ordering = ['moment']

    def __str__(self):
        return self.name + ' from ' + self.blog.name

    def get_absolute_url(self):
        return reverse('blog:article:article', kwargs={'pk': self.blog.pk,
                                                       'id': self.pk})
