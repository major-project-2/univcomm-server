from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from app import crud, models, schemas
from app.api import deps

from fastapi import WebSocket, WebSocketDisconnect

from app.websocket.init_ws import manager


from datetime import datetime
import json

from app import constants

router = APIRouter()


@router.websocket("/ws/{user_id}/{role_id}")
async def websocket_endpoint(
        websocket: WebSocket, user_id: int, role_id: int):
    await manager.connect(websocket)
    try:
        while True:
            print(manager.active_connections)
            # data = await websocket.receive_text()
            data = await websocket.receive_json()
            event = data['event']
            to_send = {
                "data": {},
                "message": ""
            }
            match event:
                case "ADMIN_CONNECTED":
                    to_send["message"] = data["message"]
                    await manager.send_personal_message(to_send, websocket)
                case "CLIENT_CONNECTED":
                    to_send["message"] = data["message"]
                    await manager.send_personal_message(to_send, websocket)
                case "ACCOUNT_CREATED":
                    to_send["message"] = data["message"]
                    to_send['data']['user'] = data['user']
                    await manager.send_to_admin(to_send)
                case "ACCOUNT_VERIFIED":
                    to_send["message"] = data["message"]
                    to_send['data']['user_id'] = data['user_id']
                    await manager.send_to_user(to_send)
                case default:
                    print("Invalid event")
            # await manager.broadcast(f"Broadcast - {constants.role_dict[role_id]} {data}")
            # await manager.broadcastButAdmin(f"Broadcast but Admin - {constants.role_dict[role_id]} {data}")
            # await manager.sendToAdmin(f"Admin - You wrote: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{constants.role_dict[role_id]} left the chat")
