

import logging

logging.basicConfig(filename='C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\logfile.log',
                    level = logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#logging.debug("This is debug logging")
logging.info("This is info logging")
logging.warning("This is warning logging")
logging.error("This is Error logging")
#logging.critical("This is critical logging")

