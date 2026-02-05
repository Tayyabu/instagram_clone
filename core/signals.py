from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from .models import Post


@receiver(post_save, sender=Post)
def set_posts_permissions(sender, instance, created, **kwargs):
    if created and instance.author:
        assign_perm("view_post", instance.author, instance)
        assign_perm("change_post", instance.author, instance)
        assign_perm("delete_post", instance.author, instance)
        assign_perm("can_off_comments", instance.author, instance)
