from django.urls import path

from . import views

urlpatterns = [
        path('',views.get_index_page),

        path('room/<str:room_name>',views.get_chat_room_page)
        ]
