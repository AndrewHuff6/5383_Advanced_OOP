import asyncio
import json
import time
import websockets
from websockets.asyncio.server import serve

async def handler(websocket):
    print("Client connected")
    try:
        # Greet the new client
        await websocket.send(json.dumps({"type": "welcome", "text": "Connected to the server!"}))

        async for raw in websocket:
            msg = json.loads(raw)

            if msg["type"] == "greeting":
                reply = {"type": "reply", "text": f"Hello, {msg['name']}!"}
            elif msg["type"] == "ping":
                reply = {"type": "pong", "time": int(time.time() * 1000)}
            else:
                reply = {"type": "error", "text": "Unknown message type"}

            await websocket.send(json.dumps(reply))

    except websockets.ConnectionClosedError as err:
        print("Socket error:", err)
    finally:
        print("Client disconnected")

async def main():
    async with serve(handler, "localhost", 8080):
        print("Server running on ws://localhost:8080")
        await asyncio.get_running_loop().create_future()

asyncio.run(main())