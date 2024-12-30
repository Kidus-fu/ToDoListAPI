from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ExampleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(json.dumps({'message': 'WebSocket connected!'}))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(json.dumps({'message': f"You sent: {data}"}))
