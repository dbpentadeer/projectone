import logging
import re
import sys
from typing import Any, Dict, Optional, Tuple

def setup_logger(name: str = "app", level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a consistent logger with professional formatting.

    Args:
        name: The name of the logger. Defaults to "app".
        level: The logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: A configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if the logger is already configured
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        # Premium and high-readability log format
        formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def sanitize_name(name: Optional[str]) -> str:
    """Sanitizes an input string by removing special characters and excess whitespace.

    This ensures that inputs are clean and safe for processing.

    Args:
        name: The name string to sanitize.

    Returns:
        str: The sanitized, cleaned name string. Defaults to 'World' if input is empty or invalid.
    """
    if not name or not isinstance(name, str):
        return "World"

    # Remove non-alphanumeric and non-space characters
    cleaned = re.sub(r"[^\w\s-]", "", name)
    # Collapse multiple spaces and strip leading/trailing whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    return cleaned if cleaned else "World"


def api_response(success: bool, message: str, data: Optional[Any] = None, status_code: int = 200) -> Tuple[Dict[str, Any], int]:
    """Generates a standardized JSON response tuple for Flask APIs.

    Args:
        success: Whether the operation succeeded.
        message: A descriptive message explaining the outcome.
        data: Optional payload returning data.
        status_code: HTTP status code. Defaults to 200.

    Returns:
        Tuple[Dict[str, Any], int]: Dict with success, message, data fields and the status code.
    """
    response_payload = {
        "success": success,
        "message": message,
        "data": data or {}
    }
    return response_payload, status_code

