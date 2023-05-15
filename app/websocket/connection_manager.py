from fastapi import WebSocket
from typing import List


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self,  data: dict, websocket: WebSocket):
        await websocket.send_json(data)

    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            await connection.send_json(data)

    async def broadcast_but_admin(self, data: dict):
        for connection in self.active_connections:
            if int(connection.scope['path_params']['role_id']) != 0:
                await connection.send_json(data)

    async def send_to_admin(self, data: dict):
        for connection in self.active_connections:
            if int(connection.scope['path_params']['role_id']) == 0:
                await connection.send_json(data)

    async def send_to_user(self, data: dict, user_id: int):
        for connection in self.active_connections:
            if int(connection.scope['path_params']['user_id']) == user_id:
                await connection.send_json(data)
