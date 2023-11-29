import asyncio
import json
import random
from quart import websocket, Quart

app = Quart(__name__)

commands = ["start", "bolt-start", "bolt-end", "end"]
# commands = ["start", "bolt-start", "bolt-end", "bolt-start", "bolt-end", "bolt-start", "bolt-end", "bolt-start", "bolt-end", "end"]

@app.websocket("/")
async def random_data():
    for i in commands:
        await asyncio.sleep(3)
        await websocket.send(i)


if __name__ == "__main__":
    app.run(port=5000)