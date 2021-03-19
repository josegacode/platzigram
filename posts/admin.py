from django.contrib import admin
from posts.models import Post
# Register your models here.

# For check posts in admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'photo', )

admin.site.register(Post, PostAdmin)
