from django.conf import settings
from django.db.models.signals import  pre_delete
from django.dispatch import receiver

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from guardian.models import UserObjectPermission, GroupObjectPermission




@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_obj_perms_connected_with_user(sender, instance, **kwargs):
    filters = Q(
        content_type=ContentType.objects.get_for_model(instance), object_pk=instance.pk
    )
    UserObjectPermission.objects.filter(filters).delete()
    GroupObjectPermission.objects.filter(filters).delete()


pre_delete.connect(
    remove_obj_perms_connected_with_user,
)
