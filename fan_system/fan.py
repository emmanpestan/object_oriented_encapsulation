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

    def set_radius(self, radius):
            if radius <= 0:
                raise ValueError("Radius must be positive.")
            self.__radius = radius

    def get_radius(self):
            return self.__radius

    def set_color(self, color):
            if not color:
                raise ValueError("Color cannot be empty.")
            self.__color = color

    def get_color(self):
            return self.__color

    def set_on(self, on):
            if not isinstance(on, bool):
                raise ValueError("On must be True or False.")
            self.__on = on

    def is_on(self):
            return "ON" if self.__on else "OFF"