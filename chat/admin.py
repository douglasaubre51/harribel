from django.contrib import admin

from .models import ChannelGroup,Message

# Register your models here.
admin.site.register(ChannelGroup)
admin.site.register(Message)
