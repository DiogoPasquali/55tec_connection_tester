import logging
from datetime import date


class Logger:

    def __init__(self, path, filename=date.today().strftime('%Y-%m-%d')):
        self.path = path
        logging.basicConfig(filename=f'{self.path}/{filename}.log', level=logging.ERROR,
                            format='%(asctime)s [%(levelname)s]: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def log(message):
        logging.info(message)

    @staticmethod
    def exception(message):
        logging.exception(message)

