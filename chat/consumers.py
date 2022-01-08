# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        Content = text_data_json['Content']
        WhoSend = text_data_json['WhoSend']
        Date = text_data_json['Date']
        M_Id = text_data_json['M_Id']
        MakeDealU = text_data_json['MakeDealU']
        MakeDealOU = text_data_json['MakeDealOU']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'Content': Content,
                'WhoSend': WhoSend,
                'Date': Date,
                'M_Id':M_Id,
                'MakeDealU': MakeDealU,
                'MakeDealOU':MakeDealOU,


            }
        )


    # Receive message from room group
    def chat_message(self, event):
        Content = event['Content']
        WhoSend = event['WhoSend']
        Date = event['Date']
        M_Id = event['M_Id']
        MakeDealU = event['MakeDealU']
        MakeDealOU = event['MakeDealOU']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'Content': Content,
            'WhoSend': WhoSend,
            'Date':Date,
            'M_Id':M_Id,
            'MakeDealU':MakeDealU,
            'MakeDealOU':MakeDealOU,

        }))
