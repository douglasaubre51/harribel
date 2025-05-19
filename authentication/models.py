from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils import timezone

# Create your models here.
class Account(AbstractUser):
    pass

class Message(models.Model):
    created_at = models.DateTimeField( default = timezone.now )

    text = models.CharField( max_length = 255 )

    sender = models.ForeignKey(
            Account,
            related_name = 'chats',
            on_delete = models.CASCADE
            )

