import logging
import os

class ExitOnCritical(logging.Handler):
    def emit(self, record):
        
        if record.levelno in (logging.CRITICAL,):
            exit(-1)

def get_logger(level: str = 'INFO'):

    log = logging.getLogger('SafeSnapraid')
    
    log.setLevel(level=os.getenv('LOG_LEVEL', level).upper())
    
    # define handler and formatter
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

    # add formatter to handler
    handler.setFormatter(formatter)

    # add handler to logger
    log.addHandler(handler)

    log.addHandler(ExitOnCritical())  


    return log
    

