

import logging


logging.basicConfig(filename='C:\\Users\\AL02673\\OneDrive - Elevance Health\\Documents\\del\\division.log',
                    level = logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def division():
    try:
        logging.info("the execution method started")
        a  = int(input())
        b  = int(input())
        logging.info(f"the values of a and b are {a} and {b}")
        div = a//b
        logging.info(f"the result is {div}")
        logging.info("the execution method end")
    except Exception as e:
        logging.error(f" fatal error occured : {e}")


logging.info("the method call stared")
division()
logging.info("the method call ended")


p02_m01_trees.py
from prabhakarSir.OOPs.package01.p01_m01_fruits import fruit02
import prabhakarSir.OOPs.package01.p01_m01_fruits as f


print(f.fruit01)
print(fruit02)

