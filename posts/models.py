from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _lazy


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Usuario")
    image = models.ImageField(_lazy("Imagen"), upload_to="posts_images/")
    description = models.TextField(_lazy("Comentario"), max_length=500,blank=True)
    created_at = models.DateTimeField(_lazy("Fecha de creacion"), auto_now_add=True)
    likes = models.ManyToManyField(User, verbose_name=_lazy("Nº de likes"),related_name='liked_posts', blank=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
    
class Comments(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(_lazy("Comentario"), max_length=300)
    created_at = models.DateTimeField(_lazy("Fecha de creacion"), auto_now_add=True)
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f"Comentó {self.user.username} el post {self.post}"
