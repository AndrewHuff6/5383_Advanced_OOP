# Quick check that server.py works, with no Pygbag or browser involved.
# Run server.py in one terminal, then run this in another.

import asyncio
import json
import websockets


async def main():
    async with websockets.connect("ws://localhost:8765") as ws:
        message = await ws.recv()
        state - json.loads(message)
        print("State received from server: ")
        for key, valu in state.items():
            print(f"{key}: {value}")



asyncio.run(main())