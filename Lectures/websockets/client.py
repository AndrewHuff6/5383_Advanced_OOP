import asyncio
import json
from websockets.asyncio.client import connect

async def main():
    async with connect("ws://localhost:8080") as ws:
        print("Connected! state:", ws.state.name)  # OPEN

        await ws.send(json.dumps({"type": "greeting", "name": "Alex"}))
        await ws.send(json.dumps({"type": "ping"}))

        # We expect three messages back: welcome, reply, pong
        for _ in range(3):
            msg = json.loads(await ws.recv())

            if msg["type"] in ("welcome", "reply"):
                print("Server says:", msg["text"])
            elif msg["type"] == "pong":
                print("Pong received at", msg["time"])
            else:
                print("Other message:", msg)

    print("Connection closed")

asyncio.run(main())