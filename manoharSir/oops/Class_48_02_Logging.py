

#print have limitation of once the job completed we do not have the execution of the flow.
# print cannotmaintain the history of the flow
# logging will store the job history in a file



#Debug: to debug at every step we use debug, to diagnose theproblem we use it
#info : it is most commenely used to capture the track of each step
#warning : to get the warnings
#Error :
#critical :

import logging

logging.basicConfig(level =  logging.DEBUG)

logging.debug("This is debug logging")
logging.info("This is info logging")
logging.warning("This is warning logging")
logging.error("This is Error logging")
logging.critical("This is critical logging")

logging.info(f"Extracted records count for load_run_id : '1234' -> {{ prcs_header: '1234', df_MergedHeadDetailTrailer: '1234', prcs_trailer: '1234'  }}")
