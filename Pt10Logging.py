# Logging :
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%MM:%S')
import helper


# can log to 5 diff log levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
# by default onl warning or above are printed
# can change immediatly after the importing of the module
# OUTPUTS
# 11/03/2021 17:03M:25 - root - DEBUG - This is a debug message
# 11/03/2021 17:03M:25 - root - INFO - This is an info message
# 11/03/2021 17:03M:25 - root - WARNING - This is a warning message
# 11/03/2021 17:03M:25 - root - ERROR - This is an error message
# 11/03/2021 17:03M:25 - root - CRITICAL - This is a critical message

# to access the own logger call the logger object made in the helper file
helper.logger.debug('This is a debug message')
helper.logger.info('This is an info message')
helper.logger.warning('This is a warning message')
helper.logger.error('This is an error message')
helper.logger.critical('This is a critical message')

# LOG HANDLERS - differnt handlers to send different messages
logger = logging.getLogger(__name__)

# make handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')
# set level
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
# set format
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# add handler to the logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error("This is an error")

# USING DICT CONFIG METHOD