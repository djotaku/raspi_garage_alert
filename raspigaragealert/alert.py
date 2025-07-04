import logging
import socket
import xdgenvpy

from raspigaragealert import garage_door as door
from raspigaragealert.services import mqtt
from raspigaragealert.services import matrix

logging.basicConfig(level=logging.INFO, format='%(levelname)s - Main Loop - %(asctime)s - %(message)s')


def check_matrix(server):
    try:
        host = socket.gethostbyname(server)
        connection = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

def main():
    xdg = xdgenvpy.XDGPedanticPackage('raspigaragealert')
    my_door = door.door(7)
    mqtt_service = mqtt.Publisher(xdg) 
    my_matrix_bot = matrix.MatrixBot(xdg)
    loop = True
    success = False
    while loop:
        door_state_changed, state_in_words = my_door.has_state_changed()
        if door_state_changed:
            logging.info(f"Garage door is now {state_in_words}.")
            success = mqtt_service.publish(state_in_words)
            my_matrix_bot.main(f"Garage door is now {state_in_words}.")
        if not success:
            success = mqtt_service.publish(state_in_words)
        # loop = False


if __name__ == "__main__":
    main()
