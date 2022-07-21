import asyncio
import datetime
import random
import websockets
import json

WS_MESSAGE = {
  "type": "EXAMPLE", # type of message
  "data": { # data object
  }
}

config = {
  "host": "localhost",
  "port": 8765
}

async def test(websocket, path):
  while True:
    input('Press "Enter" to send message.')
    payload = json.dumps(WS_MESSAGE)
    await websocket.send(payload)

start_server = websockets.serve(test, config.host, config.port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
