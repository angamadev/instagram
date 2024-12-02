from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _lazy
from easy_thumbnails.fields import ThumbnailerImageField



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',verbose_name=_lazy("Usuario"),)
    profile_picture = ThumbnailerImageField(_lazy('Imagen de perfil'), upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(_lazy('Biografía'), max_length=500, blank=True)
    birth_date = models.DateField(_lazy('Fecha de nacimiento'), null=True, blank=True)
    followers = models.ManyToManyField("self",symmetrical=False,related_name='following',through='Follow')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        
    def __str__(self):
        return self.user.username
    
    def follow(self, profile):
        Follow.objects.get_or_create(follower=self, following=profile)
    
    
class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, verbose_name=_lazy("Seguidor"), on_delete=models.CASCADE, related_name="follower_set")
    following = models.ForeignKey(UserProfile, verbose_name=_lazy("Siguiendo a"), on_delete=models.CASCADE,related_name="following_set")
    created_at = models.DateTimeField(_lazy("Desde cuando lo sigue"), auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'following')
        verbose_name = _lazy('Seguidor')
        verbose_name_plural = _lazy('Seguidores')

    def __str__(self):
        return f"{self.follower} follows {self.following}"