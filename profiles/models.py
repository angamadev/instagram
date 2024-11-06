from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField('Imagen de perfil', upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField('Biografía', max_length=500, blank=True)
    birth_date = models.DateField('Fecha de nacimiento', null=True, blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name='following', through='Follow')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user.username
    
    
class Follow(models.Model):
    following = models.ForeignKey(UserProfile, verbose_name="Siguiendo a", on_delete=models.CASCADE,related_name="following_set")
    follower = models.ForeignKey(UserProfile, verbose_name="Seguidor", on_delete=models.CASCADE, related_name="follower_set")
    created_at = models.DateTimeField("Desde cuando lo sigue", auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'following')
        verbose_name = 'Seguidor'
        verbose_name_plural = 'Seguidores'

    def __str__(self):
        return f"{self.follower} follows {self.following}"