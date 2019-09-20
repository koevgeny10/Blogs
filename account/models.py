from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# from bloging.models import Blogs

#from django.db.models.signals import post_save
#from django.dispatch import receiver


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
    # subscribes = ArrayField(models.TextField(), null=True)
    moment = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'moment'
        ordering = ['moment']

    def __str__(self):
        return self.username.username


#@receiver(post_save, sender=User)
#def createUserProfile(sender, instance, created, **kwargs):
#    if created:
#        Profile(username=instance).save()
