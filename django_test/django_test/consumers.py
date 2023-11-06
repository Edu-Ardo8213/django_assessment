from channels.generic.websocket import AsyncWebsocketConsumer
import json
from webApp.models import customer, payments_customer
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import random
import asyncio

class CreateCustomerConsumer(AsyncWebsocketConsumer):
	websocket_path = "ws/create_customer/"  # Ruta del WebSocket

	async def connect(self):
		await self.accept()
		
		while True:
			await asyncio.sleep(2)  # Espera 5 segundos
			random_number = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
			await self.send(text_data=json.dumps({'number': random_number}))


