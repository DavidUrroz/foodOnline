from .models import User, UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, *args, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            
        except Exception as e:
            #Create the user profile if not exists
            UserProfile.objects.create(user=instance)
            print('Profile did not exist, It was created')
        print('User is updated')


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, *args, **kwargs):
    print(instance.username, 'this user isbeing saved')