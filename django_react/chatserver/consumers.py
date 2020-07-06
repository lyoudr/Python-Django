from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from piano.models import Chat_Table, Users
from channels.layers import get_channel_layer
import json 
import logging

logger = logging.getLogger('django')
logger.debug('msg')

class ChatConsumer(WebsocketConsumer):
  # Called on connection.
  def connect(self):
    
    print('self.scope is =>', self.scope)
    self.name = self.scope['url_route']['kwargs']['user']
    group_list = self.name.split('-')
    group_list.sort()
    print('group_list is =>', group_list)
    self.group_name = group_list[0] + '-' + group_list[1]
    print('group_name is =>', self.group_name)
    logger.debug('connect')
    
    # Join group group_add('group_name', 'channel_name')
    async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
    
    # To accept the connection call:
    self.accept('echo-protocol')
    print('accept!')
    self.send('connected!')
    # Send message to room group
    async_to_sync(self.channel_layer.group_send)(
      self.group_name,
      {
        'type': 'chat_message',
        'message': 'Join group'
      }
    )

  def disconnect(self, close_code):
    async_to_sync(self.channel_layer.group_discard)(
      self.group_name,
      self.channel_name
    )
  
  # Receive message from WebSocket
  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    print('text_data is =>', text_data_json)
    sender = Users.objects.get(username = text_data_json['who_send'])
    print('sender is =>', sender)
    message = sender.chats.create(who_send = sender, who_receive = text_data_json['person'], message = text_data_json['message'], time = text_data_json['time'])
    # message = Chat_Table(who_send = sender, who_receive = text_data_json['person'], message = text_data_json['message'], time = text_data_json['time']) 
    print('message is =>', message)
    # Send message to chat group
    async_to_sync(self.channel_layer.group_send)(
      self.group_name,
      {
        'type': 'chat_message',
        'who_send': text_data_json['who_send'],
        'message': text_data_json['message'],
        'time': text_data_json['time'],
        'person': text_data_json['person']
      }
    )
  
  # Receive message from chat group
  def chat_message(self, event):
    print('event is =>', event)

    # Send message to WebSocket
    if event['message'] != 'Join group':
      self.send(text_data = json.dumps(event))

