import xdgenvpy

from raspigaragealert import garage_door as door
from raspigaragealert.services import mqtt
from raspigaragealert.services import matrix


def main():
    xdg = xdgenvpy.XDGPedanticPackage('raspigaragealert')
    my_door = door.door(7)
    mqtt_service = mqtt.Publisher(xdg)  # testing values - will need to make user configurable
    my_matrix_bot = matrix.MatrixBot(xdg)
    loop = True
    success = False
    while loop:
        door_state_changed, state_in_words = my_door.has_state_changed()
        if door_state_changed:
            print(f"Garage door is now {state_in_words}.")
            success = mqtt_service.publish(state_in_words)
            my_matrix_bot.main(f"Garage door is now {state_in_words}.")
        if not success:
            success = mqtt_service.publish(state_in_words)
        # loop = False


if __name__ == "__main__":
    main()
