import random

class WaterSensor:

    def read_level(self) -> int:
        return random.randint(20, 100)
