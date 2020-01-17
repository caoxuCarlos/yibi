from django.db.models.signals import post_save
from django.contrib.auth.models import User
# User here is a sender
from django.dispatch import receiver
# A recever is a function get this signal
# and perform some task.
from .models import Profile

# When the User is saved, send "post_save" signal,
# and the signal is going to be received by "@receiver",
# and the reciever is the function under decorator.
# The function takes all the arguments that "post_save" passed to it.
@receiver(post_save,sender=User) # post is the signal
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User) # post is the signal
def save_profile(sender,instance,**kwargs):
    instance.profile.save()