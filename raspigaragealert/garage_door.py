"""Class representing a Garage Door alarm."""

import RPi.GPIO as GPIO


class door():
    def __init__(self, pin: int):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.state: int = 1
        self.pin = pin
        self.state_definition = {1:"closed", 0:"open"}


    def _check_pin(self):
        current_state = GPIO.input(self.pin)
        return current_state


    def has_state_changed(self) -> tuple:
        current_state = self._check_pin()
        #print(f"For debugging: \nCurrent state: {current_state}. \nself.state: {self.state}")
        if current_state != self.state:
            self.state = current_state
            state_in_words = self.state_definition[self.state]
            return True, state_in_words
        else:
            return False, "unchanged" 
