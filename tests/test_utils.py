import logging
import pytest
from utils import sanitize_name, setup_logger


def test_setup_logger():
    """Verifies that setup_logger creates a logger with standard settings."""
    logger_name = "test_logger"
    logger = setup_logger(logger_name, level=logging.DEBUG)

    assert logger.name == logger_name
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) > 0


@pytest.mark.parametrize(
    "input_name,expected_output",
    [
        ("Alice", "Alice"),
        ("  Bob  ", "Bob"),
        ("Charlie#$!", "Charlie"),
        ("", "World"),
        (None, "World"),
        ("John   Doe", "John Doe"),
        ("Special-Char_Name", "Special-Char_Name"),
        (123, "World"),  # non-string type
    ]
)
def test_sanitize_name(input_name, expected_output):
    """Verifies that sanitize_name correctly filters input values."""
    assert sanitize_name(input_name) == expected_output


def test_api_response():
    """Verifies that api_response constructs standard JSON tuples correctly."""
    from utils import api_response
    res, code = api_response(success=True, message="Test msg", data={"key": "val"}, status_code=201)
    
    assert code == 201
    assert res["success"] is True
    assert res["message"] == "Test msg"
    assert res["data"] == {"key": "val"}

    # Test defaults
    res_def, code_def = api_response(success=False, message="Fail")
    assert code_def == 200
    assert res_def["success"] is False
    assert res_def["message"] == "Fail"
    assert res_def["data"] == {}

