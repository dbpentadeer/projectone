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


import boto3
from botocore.exceptions import BotoCoreError, ClientError

def upload_to_s3(file_obj, bucket_name: str) -> str:
    """Upload a file-like object to the given S3 bucket.
    The object key is generated from the original filename plus a timestamp to avoid collisions.
    Returns the public URL of the uploaded object (assuming the bucket allows public read).
    """
    import datetime, urllib.parse
    # Generate a safe key: original filename (if any) plus timestamp
    original_name = getattr(file_obj, "filename", getattr(file_obj, "name", "upload"))
    # Ensure no path components
    original_name = original_name.split('/')[-1]
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    key = f"{timestamp}_{original_name}"
    s3 = boto3.client('s3')  # IAM Role credentials
    try:
        s3.upload_fileobj(file_obj, bucket_name, key)
        logging.info("Uploaded %s to s3://%s/%s", original_name, bucket_name, key)
        # Build URL (public read assumed)
        url = f"https://{bucket_name}.s3.amazonaws.com/{urllib.parse.quote(key)}"
        return url
    except (BotoCoreError, ClientError) as exc:
        logging.error("Upload to S3 failed: %s", exc, exc_info=True)
        raise

