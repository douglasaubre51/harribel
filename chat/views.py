from django.shortcuts import render,redirect

# Create your views here.
def get_index_page(request):

    if request.method == 'GET':
        return render(request,'chat/index.html')


    elif request.method == 'POST':

        room_name = request.POST['room-name']
        print(f'room name is {room_name}')

        if room_name != '':
            return redirect(f'room/{ room_name }')

        else:
            return render(request,'chat/index.html')


def get_chat_room_page(request,room_name):
    return render(request,'chat/room.html',{ 'room_name' : room_name })
