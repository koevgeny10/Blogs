from django.db import models
from django.urls import reverse
from account.models import Profile


class Blogs(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        to_field='username',
        related_name='blogs',
        related_query_name='blog'
    )
    name = models.TextField(
        primary_key=True,
        error_messages={
            'unique': 'NOT UNIQUE'
        }
    )
    picture = models.ImageField(
        upload_to='blogsMainImage/%Y/%m/%d/',
        default='/default/blogsMainImage/859_big.jpg'
    )
    about = models.TextField(null=True)
    subscribe = models.ManyToManyField(Profile, through='Subscribe', related_name='a') # Кажется это все только усложняет
    moment = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'moment'
        ordering = ['moment']

    def __str__(self):
        return self.name + ' Author: ' + str(self.owner)

    def get_absolute_url(self):
        return reverse('blog:blog', kwargs={'pk': self.pk})


class Subscribe(models.Model):
    username = models.ForeignKey(Profile, on_delete=models.CASCADE, to_field='username', related_name='subscribes', related_query_name='subscribe')
    subscribe = models.ForeignKey(Blogs, on_delete=models.CASCADE, to_field='name', related_name='subscribers', related_query_name='subscriber')
    moment = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'moment'
        ordering = ['moment']
