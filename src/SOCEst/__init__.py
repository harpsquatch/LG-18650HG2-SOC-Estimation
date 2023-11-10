import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#Initialising the logging stream: Time, level, module and then message

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #Creates a log folder where the logs will be saved 
        logging.StreamHandler(sys.stdout) #Prints the logs in the terminal 
    ]
)

logger = logging.getLogger("SOCprojectlogger")