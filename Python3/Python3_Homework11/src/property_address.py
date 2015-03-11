import re
import logging

LOG_FILENAME = "property_address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "info" # Default log level
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
    # log a message
    #logging.info('Starting up the property_address program')

class Address():
    def __init__(self, name, street_address, city, state, zip_code):
        logging.info("Creating a new address")
        self._name = name
        self.street_address = street_address
        self.city = city
        self._state = state
        self._zip_code = zip_code
        
    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        state_match = re.match(r"[A-Z]{2}", value)
        if state_match: 
            self._state = value
        else:
            logging.error("STATE exception")
            raise StateError()
        
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        zip_match = re.match(r"\d{5}", value)
        if zip_match and len(value) == 5:
            self._zip_code = value
        else:
            logging.error("ZIPCODE exception")
            raise ZipCodeError()
            

class ZipCodeError(Exception):
    #def __init__(self):
        #self.msg = "ZIPCODE exception"
    def ZipCodeError(self):
        #msg = "ZIPCODE exception"
        #logging.error(self.msg)
        pass

class StateError(Exception):
    def StateError(self):
        #msg = "STATE exception"
        #logging.error(msg)
        pass
    


