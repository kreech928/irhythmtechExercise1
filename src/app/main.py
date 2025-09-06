import logging
import time
import random

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../monitor.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DMMSerial:
    def __init__(self, port: str, baudrate: int):
        self.port = port
        self.baudrate = baudrate

    @staticmethod
    def mocked_get_vh1():
        return random.uniform(0.0, 1.8)

    @staticmethod
    def mocked_get_vh2():
        return random.uniform(0.0, 1.8)


def monitor_v_temp(threshold: float, i: int = 10, interval: float = 1.0, dmm: DMMSerial | None = None) -> bool:
    dmm = dmm or DMMSerial("COM3", 115200)

    for idx in range(i):
        vh1 = dmm.mocked_get_vh1()
        vh2 = dmm.mocked_get_vh2()
        diff = abs(vh1 - vh2)

        logger.info(f"Iteration {idx}: vh1={vh1:.3f} V, vh2={vh2:.3f} V, diff={diff:.3f} V")

        if diff > threshold:
            logger.error(f"Temperature variation exceeded threshold! diff={diff:.3f} V > {threshold:.3f} V")
            return False

        time.sleep(interval)

    return True
