import logging
from logging import handlers

class LogGeneration:

    @staticmethod
    def logGen():
        handler_logger = logging.FileHandler(filename=".\\Logs\\automation1.log", mode='w')
        # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(message)s", filename=".\\Logs\\automation1.log", mode='w')
        handler_logger.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler_logger)
        return logger