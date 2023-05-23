import logging
# create and configure logger


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.log", format='%(asctime)s: %(levelname)s: %(massage)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()  # create logger object with configuration and name
        logger.setLevel(logging.INFO)  # Default logger level is logging.WARNING
        return logger




