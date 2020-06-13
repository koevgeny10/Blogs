from django.db import models
from django.urls import reverse
from profile.models import Profile


class Blog(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='blogs',
        related_query_name='blog'
    )
    name = models.TextField(
        unique=True,
        error_messages={
            'unique': 'NOT UNIQUE'
        }
    )
    picture = models.ImageField(
        upload_to='blogs_picture/%Y/%m/%d/',
        default='/default/blogs_main_image/859_big.jpg'  # TODO !
    )
    about = models.TextField(null=True)
    subscribe = models.ManyToManyField(
        Profile,
        through='Subscribe',
        related_name='a'
    )
    moment = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'moment'
        ordering = ['moment']

    def __str__(self):
        return f'{self.name} Author: {self.owner}'

    def get_absolute_url(self):
        return reverse('blogs:blog', kwargs={'blog_id': self.id})


class Subscribe(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='subscribes',
        related_query_name='subscribe'
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='subscribers',
        related_query_name='subscriber'
    )
    moment = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'moment'
        ordering = ['moment']
