from tkinter import N
from django.db import models
from accounts.models import User

# Create your models here.


class Post(models.Model):
    content = models.TextField()
    likes = models.ManyToManyField(User, through="PostLikes")
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    file = models.FileField(upload_to="posts/")
    can_comment = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f"'{self.content if len(self.content) < 10 else self.content[0:10]}' of user {self.author.username}"

    class Meta:
        permissions = [
            ("can_publish_post", "Can publish a post"),
            ("can_feature_post", "Can feature a post"),
            ("can_off_comments", "Can off the comments"),
        ]


class Comment(models.Model):
    content = models.TextField()
    likes = models.ManyToManyField(User, through="CommentLikes")
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)

    reply_to = models.ForeignKey(
        "self", related_name="replies", on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"'{self.content if len(self.content) < 10 else self.content[0:10]}' of user {self.author.username}"


class CommentLikes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class PostLikes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
