import logging

log_level = logging.DEBUG

logging_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=log_level, format=logging_format)
logger = logging.getLogger(__name__)

