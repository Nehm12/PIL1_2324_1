# # chat/consumers.py
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from .models import Message
# from django.contrib.auth.models import User

# class PrivateChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.other_username = self.scope['url_route']['kwargs']['username']
#         self.receiver = await database_sync_to_async(User.objects.get)(username=self.other_username)
#         self.room_group_name = f'private_{self.scope["user"].username}_{self.receiver.username}'

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         user = self.scope['user']

#         await database_sync_to_async(Message.objects.create)(
#             sender=user, receiver=self.receiver, content=message)

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#                 'user': user.username,
#             }
#         )

#     async def chat_message(self, event):
#         message = event['message']
#         user = event['user']

#         await self.send(text_data=json.dumps({
#             'message': message,
#             'user': user,
#         }))

# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Message

class PrivateChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.other_user = self.scope['url_route']['kwargs']['username']
        self.room_name = f'private_{self.scope["user"].username}_{self.other_user}'
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        sender = self.scope['user']
        receiver = await database_sync_to_async(User.objects.get)(username=self.other_user)

        await database_sync_to_async(Message.objects.create)(
            sender=sender, receiver=receiver, content=message
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))
