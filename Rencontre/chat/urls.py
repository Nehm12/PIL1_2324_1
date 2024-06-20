from django.urls import path
from chat.views import Liste_users, room, load_messages, send_message

urlpatterns = [
    path('Liste_users/', Liste_users, name='Liste_users'),
    path('room/<str:username>/', room, name='room'),
    path('chat/load_messages/', load_messages, name='load_messages'),
    path('chat/send_message/', send_message, name='send_message'),
]