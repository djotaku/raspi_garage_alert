"""Provide ability to send alerts to Matrix."""

import asyncio
import json
from nio import AsyncClient

class MatrixBot:
    """A bot to send alerts about the Garage Door to Matrix"""
    def __init__(self, xdg):
        self.xdg = xdg
        try:
            with open(f'{self.xdg.XDG_CONFIG_HOME}/matrix.conf') as file:
                self.config = json.load(file)
                print("Matrix Config loaded.")
                file.close()
        except FileNotFoundError:
            print(f"Settings not found at {self.xdg.XDG_CONFIG_HOME}")

    async def send_message(self, message:str):
        client = AsyncClient(self.config.get('server'), self.config.get('username'))
        response = await client.login(password=self.config.get("password"))
        print(f"Login response: {response}")
        print(f"Room would be: {self.config.get('room')}")
        msg_response = await client.room_send(room_id=self.config.get('room'), message_type="m.room.message",
                content={"msgtype": "m.text",
                    "body": message})
        print(f"Message Response: {msg_response}")
        await client.close()

    def main(self, message):
        asyncio.run(self.send_message(message))
        #await self.client.close()


if __name__ == "__main__":
    import xdgenvpy
    xdg = xdgenvpy.XDGPedanticPackage('raspigaragealert')
    my_matrix_bot = MatrixBot(xdg)
    my_matrix_bot.main("Test message")
