import asyncio
import ssl

import websockets
import json
import os


async def test():
    async with websockets.connect('ws://192.168.0.108:3000/') as websocket:
        ji = {
            "isfirst": "true",
            "device": "pc"
        }
        await websocket.send(json.dumps(ji))
        while True:
            response = await websocket.recv()
            response = json.loads(response)
            conection = response["conection"]
            print(response)

            if conection == "true":
                print("Connection Established")
                devices = json.loads(response["devices"])
                print(f"Mobile: {devices['mobile']}\tPC: {devices['pc']}\tESP: {devices['ESP']}")

            elif conection == "newConnection" or conection == "lost":
                devices = json.loads(response["devices"])
                print(f"Mobile: {devices['mobile']}\tPC: {devices['pc']}\tESP: {devices['ESP']}")
            elif conection == "alreadyConected":
                break
            elif conection == "message":
                print("response")
                if response["message"] == "teamviewer":
                    os.startfile("C:\\Program Files\\TeamViewer\\TeamViewer.exe")
                elif response["message"] == "jupyternotebook":
                    os.startfile("C:\\Users\\Madwesh\\PycharmProjects\\pysocket\\jupyter.bat")


asyncio.get_event_loop().run_until_complete(test())
