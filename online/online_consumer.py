from channels.generic.websocket import WebsocketConsumer
from rest_framework.authtoken.models import Token
from online.models import SocketConnection
from asgiref.sync import async_to_sync
from channels.auth import login
import json
import uuid
import sys


class OnlineConsumer(WebsocketConsumer):
    token = None
    sid = None
    def connect(self):
        print('Connnect!!!')
        self.accept()
        self.send(text_data=json.dumps({ \
            'type': 'online:ping', \
            'payload': 'ping from server' \
            } \
        ))

    def disconnect(self, close_code):
    # Channel.objects.filter(name=self.channel_name).delete()
        print('DISCONNECT!!! ONLINE')
        try:
            con = SocketConnection.objects.get(sid = self.sid)
            profile = con.user
            con.delete()
            profile.update_online()
        except:
            pass

    def receive(self, text_data):
        message = json.loads(text_data)
        if message['action'] == 'login':
            print(message)
            #sys.exit()
            t = Token.objects.get(key=message['data']['token'])
            self.token = t.key
            self.sid = uuid.uuid1()
            profile = t.user.profile
            async_to_sync(login)(self.scope, profile)
            self.scope["session"].save()
            print('User login %s token %s' % (profile, message['data']['token']) )

            SocketConnection.create_if_not_exist( { \
                'user': profile, \
                'token': self.token, \
                'sid': self.sid, \
                'agent': message['data']['userAgent'] \
                })
            async_to_sync(self.channel_layer.group_add)(self.token, self.channel_name)
            profile.update_online()
        
