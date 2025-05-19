from django.db import models

# Create your models here.
class ChannelGroup(models.Model):
    channel_name = models.CharField(max_length = 50)


class Message(models.Model):
    sender_name = models.CharField(max_length = 50)

    channel_group = models.ForeignKey(
            ChannelGroup,
            on_delete = models.CASCADE
            )

    text = models.CharField(max_length = 255)

    sent_at = models.DateTimeField(auto_now_add = True)
