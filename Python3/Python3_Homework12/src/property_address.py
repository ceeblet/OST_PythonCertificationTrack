from optparse import OptionParser
import configparser
import re
import logging
import sys

config = configparser.RawConfigParser()
config.read('V:/workspace/Python3_Homework12/src/property_address.cfg')

LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')
#LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
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
        state_validator = config.get('validators', 'state')
        #state_match = re.match(r"[A-Z]{2}", value)
        state_match = re.match(state_validator, value)
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
        #zip_match = re.match(r"\d{5}", value)
#        if self.check_zip(value):
#            self._zip_code = value
#        else:
#            logging.error("ZIPCODE exception")
#            raise ZipCodeError()
        logging.debug("zip_code: value is {0}".format(value))
        self._zip_code = self.check_zip(value)
    
    def check_zip(self, value):
        zip_validator = config.get('validators', 'zip_code')
        #zip_match = re.match(r"\d{5}", value)
        zip_match = re.match(zip_validator, value)
        #if zip_match and len(value) == 5:
        if zip_match:
            return value
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

def main(options):
    add_address = None
    add_address = Address(name=options.name, street_address=options.address, city=options.city, state=options.state, zip_code=options.zip_code)
    print(add_address.name)

if __name__ == '__main__':
    usage = "Usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option('-l', '--level', dest="level", action="store", default="info", help="Sets the log level to DEBUG, INFO, WARNING, ERROR and CRITICAL")
    parser.add_option('-n', '--name', dest="name", action="store", help="sets the name value of the Address object")
    parser.add_option('-a', '--address', dest="address", action="store", help="Sets the street_address value of the Address object")
    parser.add_option('-c', '--city', dest="city", action="store", help="Sets the city value of the Address object")
    parser.add_option('-s', '--state', dest="state", action="store", help="Sets the state value of the Address object")
    parser.add_option('-z', '--zip_code', dest="zip_code", action="store", help="Sets the zip_code value of the Address object")
    (options, args) = parser.parse_args()
    start_logging(level=options.level)
    # validation
    if options.address is None or options.name is None or options.city is None or options.state is None or options.zip_code is None:
        parser.error("options -n, -a, -c, -s -z are all required.")

    main(options)

