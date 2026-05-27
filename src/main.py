import sys
from flask import Flask, render_template, request, jsonify
from utils import sanitize_name, setup_logger, api_response

# Initialize our standard logger
logger = setup_logger("flask_app")

# Initialize the Flask application
# Specify template folder location explicitly to ensure it loads properly from src/
app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET"])
def index():
    """Renders the main premium dashboard page."""
    logger.info("Serving main dashboard page.")
    return render_template("index.html")


@app.route("/feature1", methods=["GET"])
def feature1():
    """Renders the morning stock watchlist dashboard page."""
    logger.info("Serving morning stocks page.")
    return render_template("feature1.html")


@app.route("/feature2", methods=["GET"])
def feature2():
    """Renders the afternoon company workstation page."""
    logger.info("Serving afternoon company page.")
    return render_template("feature2.html")



@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint to verify web application status."""
    logger.debug("Received health check request.")
    res, status_code = api_response(success=True, message="Flask server is running active", data={"status": "healthy"})
    return jsonify(res), status_code


@app.route("/api/greet", methods=["POST"])
def greet():
    """Accepts a name parameter, sanitizes it, and returns a greeting JSON payload."""
    try:
        # Gracefully handle missing JSON request body or missing 'name' parameter
        req_data = request.get_json(silent=True) or {}
        raw_name = req_data.get("name", "")

        # Sanitize using our utility function
        cleaned_name = sanitize_name(raw_name)
        greeting_message = f"Hello, {cleaned_name}! Welcome to your new Python Flask project."
        
        logger.info(f"Processed greet request for name: '{raw_name}' -> '{cleaned_name}'")
        
        res, status_code = api_response(
            success=True,
            message=greeting_message,
            data={
                "input_name": raw_name,
                "sanitized_name": cleaned_name
            }
        )
        return jsonify(res), status_code
    except Exception as e:
        logger.error(f"Error handling greet request: {e}", exc_info=True)
        res, status_code = api_response(
            success=False,
            message="Internal server error occurred.",
            status_code=500
        )
        return jsonify(res), status_code


def main() -> int:
    """Runs the Flask web server.

    Returns:
        int: The process exit status code (0 for success).
    """
    try:
        logger.info("Starting Flask development server on http://0.0.0.0:19191...")
        # Bind specifically to port 19191 as requested
        app.run(host="0.0.0.0", port=19191, debug=False)
        return 0
    except Exception as e:
        logger.critical(f"Failed to start Flask server: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())

