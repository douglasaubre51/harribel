import json
from django.shortcuts import render,redirect

from .models import ChannelGroup,Message

# Create your views here.
def get_index_page(request):
    # load index page
    if request.method == 'GET':
        return render(request,'chat/index.html')

    # move to room
    elif request.method == 'POST':
        room_name = request.POST['room-name']

        if room_name != '':
            return redirect(f'room/{ room_name }')

        else:
            return render(request,'chat/index.html')


def get_chat_room_page(request,room_name):
    # clean up room_name for room_group_name in consumers
    room_name = "-".join(room_name.split(' '))
    
    # get room
    try:
        channel_group = ChannelGroup.objects.get(channel_name = room_name)
        
    except ChannelGroup.DoesNotExist:
        channel_group = ChannelGroup.objects.create(channel_name = room_name)
    
    # get msg history
    messages = channel_group.messages.all().values()

    # get room
    return render(request,'chat/room.html',{ 
                                            'room_name': room_name,
                                            'messages': messages
                                            })
