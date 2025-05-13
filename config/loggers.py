import logging
import sys

STANDART_FORMAT = "%(asctime)s | %(name)-20s - %(levelname)s - %(message)s"
ERROR_FORMAT = "%(asctime)s | %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

METRICS = "metrics"
ROUTERS = "routers"
APP = "app"
DB = "db"

LOGGERS = [
    METRICS,
    ROUTERS,
    APP,
    DB,
]

logging.basicConfig(
    level=logging.INFO,
    format=STANDART_FORMAT,
    datefmt=DATE_FORMAT,
)


def setup_logging() -> None:
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging.Formatter(STANDART_FORMAT, DATE_FORMAT))
    stdout_handler.setLevel(logging.INFO)
    stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(logging.Formatter(ERROR_FORMAT, DATE_FORMAT))
    stderr_handler.setLevel(logging.ERROR)

    for logger_name in LOGGERS:
        logger = logging.getLogger(logger_name)

        if logger.handlers:
            logger.handlers.clear()

        logger.addHandler(stdout_handler)
        logger.addHandler(stderr_handler)
        logger.propagate = False
