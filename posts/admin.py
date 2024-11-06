from django.contrib import admin
from posts.models import Post,Comments

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "created_at",
        "description",
    ]
    
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "created_at",
        "text",
    ]
