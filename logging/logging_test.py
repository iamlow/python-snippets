import logging
import logging.config
import yaml
import os
import sys


def test1():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # create a file handler
    handler = logging.FileHandler('test1.log')
    handler.setLevel(logging.INFO)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)

    logger.info('Hello baby')
    logger.exception('exception')


def test2():
    with open('logging.yaml') as f:
        config = yaml.load(f)

    logging.config.dictConfig(config)

    logger = logging.getLogger()
    logger.info('test!!!')


def main(args):
    test1()
    test2()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
