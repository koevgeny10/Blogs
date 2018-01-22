from django.db import models
from django.urls import reverse
from account.models import Profile


class Blogs(models.Model):
    owner = models.ForeignKey(Profile,
                              on_delete=models.CASCADE,
                              to_field='username')
    name = models.TextField(unique=True)
    picture = models.ImageField(upload_to='blogsMainImage/%Y/%m/%d/',
                                default='/default/blogsMainImage/859_big.jpg')
    about = models.TextField(null=True)
    subscribers = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name + ' Author: ' + str(self.owner)

    def get_absolute_url(self):
        return reverse('blog:blog', kwargs={'pk': self.pk})


#class Articles(models.Model):
#    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, to_field='name')
#    name = models.TextField(unique=True)
#    text = models.TextField(null=True)
#    likes = models.BigIntegerField(default=0)
#    dislikes = models.BigIntegerField(default=0)
#
#    def __str__(self):
#        return self.name + ' from ' + self.blog
#
#    def get_absolute_url(self):
#        return reverse('blogging:article', kwargs={'pk': self.blog.pk,
#                                                   'id': self.pk})
