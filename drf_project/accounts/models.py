from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
from django.contrib.auth.models import User


class OTPassword(models.Model):
    username = models.CharField(max_length=100)
    otp = models.CharField(default=0, max_length=4)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.username.title()} has OTP {self.otp}"


# class User:
#     otp = models.CharField(default=0000, max_length=4)

#     def __str__(self):
#         return f'User: {self.username.title()}'

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
