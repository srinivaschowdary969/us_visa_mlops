from us_visa1.logger import logging
from us_visa1.exception import USvisaException
import os,sys

#logging.info("welcome to our log")
try:
    a=2/0
except Exception as e:
    raise USvisaException(e,sys)