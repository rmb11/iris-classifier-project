"""
Basic application logging utilities.

Configures a file-based logger and provides a decorator
used to record prediction inputs, outputs, and errors.
"""

import logging
import os

# Make sure the logs folder exists (both locally & on CI/VM)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def action_logger(func):
    """
    Decorator used to log request input, response output
    and any errors raised by the wrapped view.
    """
    def wrapper(request, *args, **kwargs):
        try:
            # Try reading JSON
            body = request.body.decode("utf-8") if request.body else ""
            logging.info(f"[INPUT] predict_api received: {body}")

            response = func(request, *args, **kwargs)

            # Try logging prediction output (if JSONResponse)
            try:
                data = response.content.decode("utf-8")
                logging.info(f"[OUTPUT] predict_api returned: {data}")
            except:
                logging.info("[OUTPUT] predict_api returned a non-JSON response")

            return response

        except Exception as e:
            logging.error(f"[ERROR] predict_api failed: {e}")
            raise

    return wrapper