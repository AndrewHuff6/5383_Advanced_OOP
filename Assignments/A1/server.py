# Week 2 - Minimal WebSocket server
# Accepts a client, prints whatever it sends, and replies to it.
# Later weeks will import Team / GameState from this same folder.

import asyncio
import websockets

PORT = 8765


# Runs once per connected client (one coroutine per connection)
async def handler(websocket):
    print("Client connected")
    try:
        # Loops once for each message the client sends
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Server received: {message}")
    except websockets.ConnectionClosed:
        pass
    print("Client disconnected")


async def main():
    # 0.0.0.0 so other devices (or a Codespace's port forwarding) can reach the server
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print(f"WebSocket server listening on port {PORT}")
        await asyncio.Future()  # run forever


asyncio.run(main())