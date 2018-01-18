from django.db import models
from bloging.models import Blogs


class Articles(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, to_field='name')
    name = models.TextField(unique=True)
    text = models.TextField(null=True)
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name + ' from ' + self.blog
