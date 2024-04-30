import logging
import logging.config
import sys
import re
from zad1_1 import read_log, read_file

def noErrorLogs(record):
    return 0 if record.levelno < logging.ERROR else 1

def read_l_logging(log, logging_level=logging.DEBUG):
    success_login_pattern = r'session opened for user'
    failed_login_pattern = r'Failed password for'
    connection_closed_pattern = r'session closed for user'
    error_pattern = r'error'
    intrusion_attempt_pattern = r'POSSIBLE BREAK-IN ATTEMPT!'

    # Konfiguracja loggera
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'stderr': {
                'level': 'CRITICAL',
                'class': 'logging.StreamHandler',
                'stream': sys.stderr
            },
            'stdout': {
                'level': logging.getLevelName(logging_level),
                'class': 'logging.StreamHandler',
                'stream': sys.stdout
            }
        },
        'loggers': {
            '': {
                'handlers': ['stderr', 'stdout'],
                'level': logging.getLevelName(logging_level),
                'propagate': True
            }
        }
    })

    logger = logging.getLogger(__name__)
    logger.addFilter(noErrorLogs)



    line = read_log(log)
    line_description = line[-1]
    
    logging.debug("Debug:Przeczytano %d bajtów", len(log))

    if re.search(success_login_pattern, line_description) or re.search(connection_closed_pattern, line_description):
        logging.info("Info:Znaleziono log typu: Successful login or connection closed")
    
    elif re.search(failed_login_pattern, line_description):
        logging.warning("Warning:Znaleziono log typu: Failed login")
    
    elif re.search(error_pattern, line_description):
        logging.error("Error:Znaleziono log typu: Error")

    elif re.search(intrusion_attempt_pattern, line_description):
        logging.critical("Critical:Znaleziono log typu: Break-in attempt")

if __name__ == "__main__":
    i=0
    for log in read_file():
        i+=1
        if i > 10:
            break
        read_l_logging(log, logging.INFO)
