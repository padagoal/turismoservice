
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='post/',blank=True,null=True)
    title_post = models.TextField(verbose_name='Titulo',max_length=100)
    descripcion_post = models.TextField(verbose_name='Descripcion Post',default='',max_length=180)
    likes = models.IntegerField(default=0,verbose_name='Likes')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author})'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-pk']


class LikesPerUser(models.Model):
    post_liked = models.ForeignKey(Post,on_delete=models.DO_NOTHING,related_name='post_liked_by_user')
    user = models.IntegerField(default=0,verbose_name='User')

    def __str__(self):
        return f'LikesPerUser (PostLiked: {self.post_liked}, User: {self.user})'

    class Meta:
        verbose_name = 'LikePerUser'
        verbose_name_plural = 'LikesPerUser'
