import logging
import os


logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] : %(levelname)s : %(name)s : %(message)s",
)
logger = logging.getLogger("simple_web_crawler")


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

