# https://docs.python.org/2/howto/logging.html
import logging


class Logger:

    LOG_NAME = 'entertainment_center'

    @staticmethod
    def get_logger():
        entertainment_center_logger = logging.getLogger(Logger.LOG_NAME)
        entertainment_center_sh = logging.StreamHandler()
        entertainment_center_formatter = logging.Formatter(
            '%(asctime)s %(levelname)s [%(name)s] %(pathname)s:%(lineno)d: %(message)s')
        entertainment_center_sh.setFormatter(entertainment_center_formatter)
        entertainment_center_logger.addHandler(entertainment_center_sh)
        entertainment_center_logger.setLevel(logging.INFO)
        return entertainment_center_logger
