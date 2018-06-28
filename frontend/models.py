from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
Using One-To-One Link With a User Model (Profile) because we 
need to store extra information about the existing User Model that’s not related to the authentication process.
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
"""
class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ("S", "small / medium business"),
        ("E", "enterprise"),
        ("O", "organisation"),
        ("I", "individual"),

    ]
    USER_BUSINESS_CHOICES = (
        ("M", "Maker or manufacturer of physical products"),
        ("P", "Ingredient or material producer"),
        ("R", "Retailer"),
        ("A", "Auditor"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, blank=True, null=True)
    registration_number = models.CharField(max_length=30, blank=True, null=True, )
    phone_number = models.CharField(max_length=15,)
    location = models.CharField( max_length=225, blank=True, null=True, )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=2, blank=True, null=True)
    user_business = models.CharField(choices=USER_BUSINESS_CHOICES, max_length=2, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

