"""Class representing a Garage Door alarm."""


class door():
    def __init__(self, pin: int):
        self.state = "closed"
        self.pin = pin


    def has_state_changed() -> bool:
        return True
