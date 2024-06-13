import os
import argparse
import logging
from lute.app_factory import create_app
from lute.config.app_config import AppConfig

log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

config_file = AppConfig.default_config_filename()
app = create_app(config_file, output_func=lambda s: None)

def start(port):
    """
    Start the dev server with reloads on port.
    """
    def dev_print(s):
        "Print info on first load only."
        if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            return
        print(s)

    ac = AppConfig(config_file)
    dev_print(f"\ndb name: {ac.dbname}")
    dev_print(f"data: {ac.datapath}")
    dev_print(f"Running at: http://localhost:{port}\n")

    app.run(host='0.0.0.0', debug=True, port=port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start dev server lute.")
    parser.add_argument(
        "--port", type=int, default=5000, help="Port number (default: 5000)"
    )
    args = parser.parse_args()
    start(args.port)
