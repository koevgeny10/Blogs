from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    username = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
        to_field='username',
        related_name='account'
    )
    picture = models.ImageField(
        upload_to='avatars/%Y/%m/%d/',
        default='/default/avatar/avatar.png'
    )
    moment = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'moment'
        ordering = ['moment']

    def __str__(self):
        return self.username.username
