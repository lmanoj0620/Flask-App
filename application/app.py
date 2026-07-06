from flask import Flask
import logging
import time

app = Flask(__name__)

# Logging setup (writes to mounted logs directory)
logging.basicConfig(
    filename='/app/logs/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

@app.route("/")
def home():
    msg = f"User visited home page at {time.time()}"
    app.logger.info(msg)
    return "Hello from Flask App! Logs are being generated."

@app.route("/error")
def error():
    msg = f"Something went wrong at {time.time()}"
    app.logger.error(msg)
    return "Error logged!", 500

if __name__ == "__main__":
    # Run on port 5005 instead of 5000
    app.run(host="0.0.0.0", port=5005)
