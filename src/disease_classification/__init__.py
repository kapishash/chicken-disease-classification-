import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logdir = "logs"
logfilepath=os.path.join(logdir, "logs.log")
os.makedirs(logdir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(logfilepath),
        logging.StreamHandler(sys.stdout)

    ]
)

logger = logging.getLogger("disease_classification_logger")