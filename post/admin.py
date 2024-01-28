from django.contrib import admin
from .models import Post, Comment, Share, Like
# Register your models here.


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Share)
admin.site.register(Like)
