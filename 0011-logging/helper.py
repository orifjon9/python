import logging

logger = logging.getLogger(__name__)

# create handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# link handlers
logger.addHandler(stream_h)
logger.addHandler(file_h)

# log messages
logger.warning("Warning message was fired")
logger.error("An error was happen")