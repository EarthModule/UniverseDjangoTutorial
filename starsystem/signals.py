from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Star

@receiver(pre_save, sender=Star)
def my_callback(sender, instance, *args, **kwargs):
    instance.start_type = instance.start_type
    raise Exception