from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from myFitnessApp.accounts.models import FitnessAppProfile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        FitnessAppProfile.objects.create(user=instance)