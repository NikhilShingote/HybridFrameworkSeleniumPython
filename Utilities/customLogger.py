import logging


# This all Utilities files are common for every test case

class LogGen:

    @staticmethod
    def loggen():
        # Where you exactly want to generate log file mention the location
        logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
