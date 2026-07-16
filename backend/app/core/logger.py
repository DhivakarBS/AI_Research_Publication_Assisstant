import logging
from typing import Final

LOGGER_NAME: Final[str] = "researchai"


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a centralized logger instance."""
    logger = logging.getLogger(name or LOGGER_NAME)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
