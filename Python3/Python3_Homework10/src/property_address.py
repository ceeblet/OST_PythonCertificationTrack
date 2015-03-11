import re

class Address():
    def __init__(self, name, street_address, city, state, zip_code):
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
            raise ZipCodeError()
            

class ZipCodeError(Exception):
    def ZipCodeError(self):
        pass

class StateError(Exception):
    def StateError(self):
        pass
    


