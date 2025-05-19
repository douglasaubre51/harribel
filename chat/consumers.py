import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import ChannelGroup,Message


class CustomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # get room name from url
        room_name = self.scope['url_route']['kwargs']['room_name']

        # convert spaces to - for room_group_name since it doesn't like spaces!
        room_name = "-".join(room_name.split(" "))

        # get room or create room using db
        try:
            self.channel_group = await sync_to_async(ChannelGroup.objects.get)(channel_name = room_name)

        except ChannelGroup.DoesNotExist:
            self.channel_group = await sync_to_async(ChannelGroup.objects.create)(channel_name = room_name)

        self.room_group_name = self.channel_group.channel_name

        # add user to group
        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
                )

        # connect to websocket
        await self.accept()

        # send past messages
        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'send_past_messages',
                    })

    async def send_past_messages(self,event):
        # get messages from db
        messages = await sync_to_async(Message.objects.all.values)()


    # message pipeline
    async def receive(self,text_data):
        # json package
        json_text = json.loads(text_data)
        message = json_text['message']
        username = json_text['username']

        # save msg to db
        await sync_to_async(Message.objects.create)(
                channel_group = self.channel_group,
                sender_name = username,
                text = message
                )

        # send to all groups
        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'send_message',
                    'message':message,
                    'username':username
                    })


    async def send_message(self,event):
        await self.send(text_data = json.dumps({ 
                                                'message':event['message'],
                                                'username':event['username']
                                                }))
