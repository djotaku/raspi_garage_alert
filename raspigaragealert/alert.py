from raspigaragealert import garage_door as door
from raspigaragealert.services import mqtt


def main():
    my_door = door.door(16)
    mqtt_service = mqtt.Publisher("garage/door1", "tanukimario.mushroomkingdom")  # testing values - will need to make user configurable
    loop = True
    while loop:
        door_state_changed, state_in_words = my_door.has_state_changed()
        if door_state_changed:
            print(f"Garage door is now {state_in_words}.")
            mqtt_service.publish(state_in_words)
        # loop = False


if __name__ == "__main__":
    main()
