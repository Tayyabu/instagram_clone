from turtle import mode
from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Comment, Post
# Register your models here.


class CommentInline(admin.TabularInline):
        model = Comment


class PostAdmin(GuardedModelAdmin):
        pass



admin.site.register(Post, PostAdmin)