#!/usr/bin/env python

import asyncio
import signal
import os

import websockets


async def echo(websocket, path):
    while True:
        #can only emit string
        await websocket.send('ola')
        await asyncio.sleep(1)

async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(
        echo,
        host="",
        port=int(os.environ["PORT"]),
    ):
        await stop


if __name__ == "__main__":
    asyncio.run(main())