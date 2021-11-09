import logging
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('hello from helper')
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
# will make a logger with the name of the module
# best practise is not to use root logger is to make own logger
# if you