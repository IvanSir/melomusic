from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
    BaseUserManager, PermissionsMixin

from playlist.models import Playlist

class UserManager(BaseUserManager):
    '''Custom user manager'''
    def create_user(self, email, password=None, **extra_fields):
        '''Creates and saves a user using email address'''
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''Creates and saves a new super user using email address'''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom user model that support using email instead of username'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default='default')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='UsersPictures/', default='UsersPictures/default.jpg')

    objects = UserManager()

    friends = models.ManyToManyField(to='User')
    USERNAME_FIELD = 'email'
    
    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if not self.playlists.all():
            Playlist.objects.create(owner=self)        


class Comment(models.Model):
    body = models.TextField(max_length=320)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)