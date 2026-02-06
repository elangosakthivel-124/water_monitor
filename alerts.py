import logging
from config import HIGH_LEVEL, CRITICAL_LEVEL

logging.basicConfig(filename="alerts.log", level=logging.INFO)

def check_alerts(level):

    if level >= CRITICAL_LEVEL:
        logging.warning("CRITICAL WATER LEVEL: %s", level)
        return "CRITICAL"

    elif level >= HIGH_LEVEL:
        logging.info("High water level: %s", level)
        return "HIGH"

    return "NORMAL"
