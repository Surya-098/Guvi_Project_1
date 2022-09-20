import logging


def project_logger():
    # to get the name of the test case file name at runtime
    logger = logging.getLogger()
    # FileHandler class to set the location of log file
    fileHandler = logging.FileHandler('logfile.log')
    # Formatter class to set the format of log file
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    # object of FileHandler gets formatting info from setFormatter #method
    fileHandler.setFormatter(formatter)
    # logger object gets formatting, path of log file info with addHandler #method
    logger.addHandler(fileHandler)
    # setting logging level to INFO
    logger.setLevel(logging.ERROR)
    return logger
