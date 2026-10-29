# Quick check that server.py works, with no Pygbag or browser involved.
# Run server.py in one terminal, then run this in another.

import asyncio
import websockets

async def main():
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send("hello")
        reply = await ws.recv()
        print(f"Reply from server: {reply}")


asyncio.run(main())