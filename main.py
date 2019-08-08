import lxml.html as html
import os
import sys

import patterns
import settings
from settings import logger


def load_data(content):
    content = html.fromstring(content)
    return content


def load_file(file_path):
    file_path = os.path.join(settings.BASE_DIR, file_path)
    try:
        with open(file_path, "r") as f:
            content = load_data(f.read())
        return content
    except FileNotFoundError:
        logger.error("Couldn't read file '{}'. Check file path.".format(file_path))
        sys.exit(1)


def find_element(content):
    elements = content.xpath(patterns.XPATH_LEVEL_1)
    for element in elements:
        if element.xpath(patterns.XPATH_LEVEL_2):
            continue
        element_text = "".join([text.strip() for text in element.xpath("text()")])
        if element_text:
            element_path = element.getroottree().getpath(element)
            element_id = element.xpath("@id")
            element_id = element_id[0] if element_id else "Not Found"
            logger.info('Element text: "{}". Element path: "{}". Element #id: "{}"\n'.format(element_text, element_path, element_id))

def run(origin_file, other_file):
    # origin_file = load_file(origin_file)
    other_file = load_file(other_file)
    # find_element(origin_file)
    find_element(other_file)


if __name__ == "__main__":
    original_file, other_file = sys.argv[1:3]
    run(original_file, other_file)

