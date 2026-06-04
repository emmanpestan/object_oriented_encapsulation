class Fan:

    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):

        self.__speed = None
        self.__radius = None
        self.__color = None
        self.__on = None

        self.set_speed(speed)
        self.set_radius(radius)
        self.set_color(color)
        self.set_on(on)

    def set_speed(self, speed):
        if speed not in (Fan.SLOW, Fan.MEDIUM, Fan.FAST):
            raise ValueError("Invalid speed. Use SLOW, MEDIUM, or FAST.")
        self.__speed = speed

    def get_speed(self):
        if self.__speed == Fan.SLOW:
            return "SLOW"
        elif self.__speed == Fan.MEDIUM:
            return "MEDIUM"
        elif self.__speed == Fan.FAST:
            return "FAST"