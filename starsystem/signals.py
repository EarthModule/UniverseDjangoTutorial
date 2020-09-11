from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Star

@receiver(pre_save, sender=Star)
def star_receiver(sender, instance, *args, **kwargs):
    instance.start_type = instance.start_type
    print('Star is going to be saved')