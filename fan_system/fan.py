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
