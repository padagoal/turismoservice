from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name_user = models.CharField(max_length=200,default='',verbose_name='Nombres')
    lastname_user = models.CharField(max_length=200, default='', verbose_name='Apellidos')
    date_birth_user = models.DateField(verbose_name='Fecha de Nacimiento',default=None,null=True)
    telephone_user = models.CharField(verbose_name='Numero de Telefono',max_length=100,default='',null=True)
    CI_user = models.IntegerField(verbose_name='Cedula de Identidad',default=0,null=True)
    is_customer = models.BooleanField(verbose_name='Es Cliente?',default=False)

    created_at = models.DateTimeField(verbose_name='created_at',auto_now_add=True,null=True)
    created_by = models.CharField(verbose_name='created_by',default='',max_length=200,null=True)
    updated_at = models.DateTimeField(verbose_name='updated_at',auto_now_add=True,null=True)
    updated_by = models.CharField(verbose_name='updated_by',default='',max_length=200,null=True)


@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()


