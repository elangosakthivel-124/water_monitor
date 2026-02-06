import time
from sensor import WaterSensor
from database import save_level
from alerts import check_alerts
from config import POLL_INTERVAL

class WaterMonitor:

    def __init__(self):
        self.sensor = WaterSensor()

    def run(self):
        while True:
            level = self.sensor.read_level()
            save_level(level)
            status = check_alerts(level)

            print(f"Level: {level}% | Status: {status}")
            time.sleep(POLL_INTERVAL)
