import websockets
import asyncio
import json
import os
    async def update_server():
        async with websockets.connect("ws://update.ecsdatasolutions.xyz") as websocket:
            message = await websocket.recv()
            if json.loads(message) == {"msg": "update"}:
                os.system("docker-compose down")
                os.system("docker-compose up-d")
