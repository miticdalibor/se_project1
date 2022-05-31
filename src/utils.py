"""
Module logging
"""
import logging
from time import time

logging.basicConfig(filename="example.log", level=logging.DEBUG)
# create logger with 'spam_application'
logger = logging.getLogger("frunch_infinity")
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler("example.log")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
print("start logger")
print(logger)
logger.debug("application starting")


def log_time(func):
    """
    Logs info of the time it took for func to execute
    as well as time of start
    :param func: function to be logged
    :return: function with logging as info
    """

    def wrapper(*args, **kwargs):
        start = time()
        val = func(*args, **kwargs)
        end = time()
        duration = end - start
        logger.info(
            f"{func.__name__} took {duration} seconds to run at {start}"
        )
        return val

    return wrapper